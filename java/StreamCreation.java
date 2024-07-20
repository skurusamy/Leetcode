import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

public class StreamCreation {
    public static void main(String[] args) {
        Stream<String> stream1 = Stream.of("apple","banana");
        stream1.forEach(System.out::println);
        System.out.println(stream1);

        List<Integer> list1 = Arrays.asList(1,2,3);
        Stream<Integer> stream_list = list1.stream();
        stream_list.forEach(System.out::println);

        List<String> str_list = new ArrayList<String>();
        str_list.add("Tomato");
        str_list.add("Mango");
        str_list.add("Onion");

    }
}
