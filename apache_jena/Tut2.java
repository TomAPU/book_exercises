import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;

public class Tut2 extends Object {

    public static void main (String args[]) {
        String personURI = "http://somewhere/JohnSmith";
        String givenName = "John";
        String familyName = "Smith";
        String fullName = "John Smith";

        // create an empty Model
        Model model = ModelFactory.createDefaultModel();

        // create resource
        // and add the properties cascading style
        Resource johnSmith = model.createResource(personURI)
            .addProperty(VCARD.FN, fullName)
            .addProperty(VCARD.N,
                    model.createResource()
                        .addProperty(VCARD.Given, givenName)
                        .addProperty(VCARD.Family, familyName)
                    );
    }
}
