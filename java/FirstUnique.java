import java.util.HashMap;
import java.util.Map;

public class FirstUnique {
    public static void main(String[] args) {
        int[] arr = {9, 2, 3, 2, 6, 6};
        Map<Integer,Integer> hashmap = new HashMap<>();
        for(int i = 0; i< arr.length;i++){
            hashmap.put(arr[i],hashmap.getOrDefault(arr[i], 0)+1);
        }
        for(int i =0; i< arr.length;i++){
            if(hashmap.get(arr[i]) == 1){
                System.out.println(arr[i]);
                break;
            }
        }
    }
}
