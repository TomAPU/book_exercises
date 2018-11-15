import java.io.*;

import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;
import org.apache.jena.util.FileManager;

public class Tut9 extends Object {

    static final String inputFileName1 = "vc-db-3.rdf";
    static final String inputFileName2 = "vc-db-4.rdf";

    public static void main (String args[]) {
        // create an empty Model
        Model model1 = ModelFactory.createDefaultModel();
        Model model2 = ModelFactory.createDefaultModel();

        // use FileManager to find the file
        InputStream in1 = FileManager.get().open(inputFileName1);

        if (in1 == null){
            throw new IllegalArgumentException( "File: " + inputFileName1 + " not found");
        }

        InputStream in2 = FileManager.get().open(inputFileName2);

        if (in2 == null){
            throw new IllegalArgumentException( "File: " + inputFileName2 + " not found");
        }

        // read RDF/XML files
        model1.read(in1, "");
        model2.read(in2, "");

        // merge the graph
        Model model = model1.union(model2);

        model.write(System.out, "RDF/XML-ABBREV");
    }
}
