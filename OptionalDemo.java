import java.util.Optional;

public class OptionalDemo {
    
    public static void main(String[] args){
        //Instance for optional class can be created using Of, ofnullable, empty 

        //Empty -> the given string can be empty
        Optional<Object> emptyObj = Optional.empty();
        System.out.println(emptyObj);


        //Of -> Cannot have null value
        //Optional<Object> ofObj_null = Optional.of(null);
        //System.out.println(ofObj_null);

        String value = null;

        Optional<Object> ofObj = Optional.of("Sample");
        System.out.println(ofObj);

        Optional<String> ofnullableObj  = Optional.ofNullable(value);
        String after_assgnment = ofnullableObj.orElse("email.com");
        System.out.println(after_assgnment);

        System.out.println(ofnullableObj.get());
        System.out.println(ofnullableObj.isPresent());
    }

}
