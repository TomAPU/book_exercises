import org.apache.jena.query.*;
import org.apache.jena.rdf.model.*;

import java.io.*;

import org.apache.jena.vocabulary.*;
import org.apache.jena.util.FileManager;


public class JenaARQTest {
    public static void main(String[] args){
        // create an empty Model
        Model model = ModelFactory.createDefaultModel();

        // use FileManager to find the file
        InputStream in = FileManager.get().open(inputFileName);

        if (in == null){
            throw new IllegalArgumentException( "File: " + inputFileName + " not found");
        }

        model.read(in, "");
    }
}
