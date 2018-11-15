import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;

public class Tut1 extends Object {
    // some defs
    static String personURI = "http://somewhere/JohnSmith";
    static String fullName = "John Smith";

    public static void main (String args[]) {
        // create an empty Model
        Model model = ModelFactory.createDefaultModel();

        // create resource
        Resource johnSmith = model.createResource(personURI);

        // add property
        johnSmith.addProperty(VCARD.FN, fullName);

        /*
        Resource johnSmith = 
            model.createResource(personURI)
                .addProperty(VCARD.FN, fullName);
                */
    }
}
