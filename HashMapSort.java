import java.util.*;
import static java.util.Map.Entry.*;
import static java.util.stream.Collectors.*;
public class HashMapSort {
    public static void main(String[] args) {
        Map<String,Integer> hashmap = new HashMap<>();
        hashmap.put("apple",4);
        hashmap.put("mango", 2);
        hashmap.put("Pineapple", 10);

        Map asec = hashmap.entrySet().stream().sorted(comparingByValue()).collect(toMap( e1 -> e1.getKey(), e2->e2.getValue(), (e1,e2) -> e2,LinkedHashMap::new ));
        System.out.println(asec);

        Map desc = hashmap.entrySet().stream().sorted(Collections.reverseOrder(comparingByValue())).collect(toMap(e1->e1.getKey(), e2-> e2.getValue(), (e1,e2)-> e2,LinkedHashMap::new));
        System.out.println(desc);
    }
}
