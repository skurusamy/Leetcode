import java.util.Map;
import java.util.HashMap;
public class DNASequencing {
    public static void main(String[] args) {
        String s = "AGCTGAAAGCTTAGCTG";
        int k = 5;
        Map<String,Integer> hashmap = new HashMap<>();
        for(int i = 0; i< s.length()-k+1; i = i + 1){
            
            String tmp = s.substring(i, i+k);
            hashmap.put(tmp, hashmap.getOrDefault(tmp,0)+1);
            
        }
        System.out.println(hashmap);

        for(Map.Entry<String, Integer> e : hashmap.entrySet()){
            if(e.getValue() > 1) System.out.println(e.getKey());
        }
        
    }
}
