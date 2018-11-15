import java.io.*;

import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;
import org.apache.jena.util.FileManager;

public class Tut7 extends Object {

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
        //ResIterator iter = model.listResourcesWithProperty(VCARD.FN);
        ResIterator iter = model.listSubjectsWithProperty(VCARD.FN);
        if (iter.hasNext()){
            System.out.println("The database contains vcards for:");
            while (iter.hasNext()){
                System.out.println("  " + iter.nextResource()
                                                .getRequiredProperty(VCARD.FN)
                                                .getString());
            }
        } else {
            System.out.println("No vcards are found in the database");
        }
    }
}
