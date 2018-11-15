import org.apache.jena.rdf.model.*;
import org.apache.jena.vocabulary.*;

public class Tut3 extends Object {

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

        // list the statements in the Model
        StmtIterator iter = model.listStatements();

        //print out the predicate, subject, object of each statement
        while (iter.hasNext()){
            Statement stmt = iter.nextStatement();
            Resource subject = stmt.getSubject();
            Property predicate = stmt.getPredicate();
            RDFNode object = stmt.getObject();

            System.out.print(subject.toString());
            System.out.print("[" + predicate.toString() + "]=");
            if (object instanceof Resource){
                System.out.print(object.toString());
            } else {
                // object is a literal
                System.out.print(" \"" + object.toString() + "\"");
            }

            System.out.println(" .");
        }
    }
}
