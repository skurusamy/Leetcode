import java.util.HashMap;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;

public class HashMapDemo {
    public static void main(String[] args){
        Map<Integer,String> hashmap = new HashMap<>();
        hashmap.put(1,"one");
        hashmap.put(2,"two");

        System.out.println(hashmap);

        for(Map.Entry<Integer,String> entry : hashmap.entrySet()){
            System.out.println(entry.getKey() + " " +entry.getValue());
        }

        SortedMap<Integer,String> sortedMap = new TreeMap<>();
        sortedMap.put(5, "five");
        sortedMap.put(3, "three");
        sortedMap.put(4, "four");
        sortedMap.put(1, "one");

        for(SortedMap.Entry<Integer,String> e : sortedMap.entrySet()){
            System.out.println(e.getKey()+" "+e.getValue());
        }
        
    }
}
