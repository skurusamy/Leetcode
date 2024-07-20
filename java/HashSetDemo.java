import java.util.HashSet;
import java.util.Set;

public class HashSetDemo {
    public static void main(String[] args){
        Set<Integer> sets = new HashSet<>();
        sets.add(10);
        sets.add(100);
        sets.add(200);
        sets.add(10);
        System.out.println(sets);
        
    }
}
