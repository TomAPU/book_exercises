import java.io.*;

import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;
import org.apache.jena.util.FileManager;

public class Tut6 extends Object {

    static final String inputFileName = "vc-db-1.rdf";
    static final String johnSmithURI = "http://somewhere/JohnSmith";

    public static void main (String args[]) {
        // create an empty Model
        Model model = ModelFactory.createDefaultModel();

        // use FileManager to find the file
        InputStream in = FileManager.get().open(inputFileName);

        if (in == null){
            throw new IllegalArgumentException( "File: " + inputFileName + " not found");
        }

        // read the RDF/XML file
        model.read(new InputStreamReader(in), "");

        // retrieve the John Smith vcard resource from the model
        Resource vcard = model.getResource(johnSmithURI);

        //Resource name = (Resource) vcard.getRequiredProperty(VCARD.N)
        //                                .getObject();
        Resource name = vcard.getRequiredProperty(VCARD.N)
                                        .getResource();
        String fullName = vcard.getRequiredProperty(VCARD.FN)
                                        .getString();

        // add 2 nick name properties to vcard
        vcard.addProperty(VCARD.NICKNAME, "Smithy")
            .addProperty(VCARD.NICKNAME, "Adman");

        // set up the output
        System.out.println("The nicknames of \"" + fullName + "\" are:");
        StmtIterator iter = vcard.listProperties(VCARD.NICKNAME);
        while (iter.hasNext()){
            System.out.println("    " + iter.nextStatement().getObject().toString());
        }
    }
}
