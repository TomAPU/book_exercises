import java.io.*;

import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;
import org.apache.jena.util.FileManager;

public class Tut10 extends Object {

    static final String inputFileName = "vc-db-1.rdf";

    public static void main (String args[]) {
        // create an empty Model
        Model model = ModelFactory.createDefaultModel();

        // use FileManager to find the file
        InputStream in = FileManager.get().open(inputFileName);

        if (in == null){
            throw new IllegalArgumentException( "File: " + inputFileName + " not found");
        }

        model.read(in, "");

        // create a bag container
        Bag smiths = model.createBag();

        // select all the resources with a VCARD.FN property
        // whose value ends with "Smith"
        StmtIterator iter = model.listStatements(
            new SimpleSelector(null, VCARD.FN, (RDFNode) null){
                @Override
                public boolean selects(Statement s){
                    return s.getString().endsWith("Smith");
                }
            }
        );

        // add the Smith's to bag
        while(iter.hasNext()){
            smiths.add( iter.nextStatement().getSubject());
        }

        //print the graph as RDF/XML
        model.write(new PrintWriter(System.out));
        System.out.println();

        //print out the members of the bag
        NodeIterator iter2 = smiths.iterator();
        if (iter2.hasNext()){
            System.out.println("The bag contains:");
            while (iter2.hasNext()){
                System.out.println("  " + ((Resource)iter2.next())
                                            .getRequiredProperty(VCARD.FN)
                                            .getString());
            }
        } else {
            System.out.println("Empty bag");
        }
    }
}
