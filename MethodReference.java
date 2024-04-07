import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

interface Printable{
    void print(String msg);
}



public class MethodReference {
    
    void display(String msg){
        String upper = msg.toUpperCase();
        System.out.println(upper);
    }

    public static int add(int a, int b){
        return a + b;
    }
    public static void main(String[] args){
        BiFunction<Integer,Integer,Integer> biConsumer = (a,b)-> MethodReference.add(a,b);
        System.out.println(biConsumer.apply(10, 50));

        //1. Method Referencing for static method
        BiFunction<Integer,Integer,Integer> biConsumer1 =  MethodReference::add;
        System.out.println(biConsumer1.apply(100, 50));


        //2.
        //Printable is the customer functional interface. 

        MethodReference m = new MethodReference();

        Printable consumer = (msg) -> m.display(msg);
        consumer.print("Hello");


         Printable consumer1 = m::display;
        consumer1.print("Hello_method Reference");


        //3. using argument/parameter
        Function<String,String> func = (input) -> input.toLowerCase();
        System.out.println(func.apply("My day"));

        Function<String,String> func1 = String::toLowerCase;
        System.out.println(func1.apply("Argument Method Reference"));

        //4. Constructor method referencing

        List<String> fruits = Arrays.asList("Apple","Banan","Mango");
        System.out.println(fruits);

        Function<List<String>,Set<String>> fruitSet = (fruit) -> new HashSet<>(fruit);
        System.out.println(fruitSet.apply(fruits));

        Function<List<String>,Set<String>> fruitset1 = HashSet::new;
        System.out.println(fruitset1.apply(fruits));
    }

}
