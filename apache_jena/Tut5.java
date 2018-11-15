import java.io.*;

import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;
import org.apache.jena.util.FileManager;

public class Tut5 extends Object {

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

        // write the model in XML form to a file
        System.out.println("write in default XML form");
        model.write(System.out);
    }
}
