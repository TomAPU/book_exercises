import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;

public class Tut4 extends Object {

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

        // write the model in XML form to a file
        System.out.println("write in default XML form");
        model.write(System.out);
        System.out.println("");

        System.out.println("write in RDF/XML-ABBREV form");
        model.write(System.out, "RDF/XML-ABBREV");
        System.out.println("");

        System.out.println("write in N-TRIPLES form");
        model.write(System.out, "N-TRIPLES");
    }
}
