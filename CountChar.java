import java.util.*;
import static java.util.Map.Entry.*;
import static java.util.stream.Collectors.*;
public class CountChar {
    public static void main(String args[]){
        String s = "HelloWelcome";
        Map<Character,Integer> hashmap = new HashMap<>();
        for(int i = 0; i< s.length(); i++){
            hashmap.put(s.charAt(i), hashmap.getOrDefault(s.charAt(i),0)+1);
        }

        
        char min_char ='\0', max_char = '\0';
        int min_value = Integer.MAX_VALUE;
        int max_value = Integer.MIN_VALUE;

        for(Map.Entry<Character,Integer> e : hashmap.entrySet()){
            if(e.getValue() < min_value){
                min_value = e.getValue();
                min_char = e.getKey();
            }
            if(e.getValue() > max_value){
                max_value = e.getValue();
                max_char = e.getKey();
            }
        }
        System.out.println(min_char + " " + max_char);

        Map<Character,Integer> sorted_char = hashmap.entrySet().stream().sorted(comparingByValue()).collect(toMap(e1->e1.getKey(),e2->e2.getValue(),(e1,e2)->e2,LinkedHashMap::new));
        System.out.println(sorted_char);
    }
}
