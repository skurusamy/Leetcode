import java.time.LocalDate;
import java.util.function.BiFunction;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Supplier;

/*class FunctionImpl implements Function<String,String>{
    @Override
    public String apply(String msg) {
        System.out.println("In apply method");;
        return msg;
    }

}
*/

public class FunctionalInterface {
    public static void main(String[] args){
       // FunctionImpl imp = new FunctionImpl();
        //imp.apply("Hello");
        
        //Function - one input, one output
        Function<String,String> imp = (String msg) -> msg;
        System.out.println(imp.apply("Using lambda function"));

        //Consumer one input but no return type
        Consumer<String> consumerInterface = (msg) -> System.out.println(msg);
        consumerInterface.accept("Consumer Example");

        //Supplier no input but one return type
        Supplier<String> supplierInterface = () -> "Supplier Example " + LocalDate.now();
        System.out.println(supplierInterface.get());

        //BiFunction - 2 input, 1 output
        BiFunction<Integer,Integer,Integer> biFunction = (a,b) -> a+b;
        System.out.println(biFunction.apply(10, 20));

    }
}
