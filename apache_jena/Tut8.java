import java.io.*;

import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;
import org.apache.jena.util.FileManager;

public class Tut8 extends Object {

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

        // select all the resources with a VCARD.FN property
        // whose value ends with "Smith"
        StmtIterator iter = model.listStatements(
            new SimpleSelector(null, VCARD.FN, (RDFNode) null){
                public boolean selects(Statement s){
                    return s.getString().endsWith("Smith");
                }
            }
        );

        if (iter.hasNext()){
            System.out.println("The database contains vcards for:");
            while (iter.hasNext()){
                System.out.println("  " + iter.nextStatement()
                                                .getString());
            }
        } else {
            System.out.println("No vcards are found in the database");
        }
    }
}
