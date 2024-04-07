import java.util.HashMap;
import java.util.Map;

public class IsSubSetArr {
    public static void main(String[] args) {
        int[] arr1 = {9,4,7,1,-2,6,5};
        int[] arr2 = {10,12};
        Map<Integer,Integer> hashmap = new HashMap<>();
        for(int e :arr1){
            hashmap.put(e, hashmap.getOrDefault(hashmap.get(e), 0)+1);
        }
        for(int e: arr2){
             if(hashmap.containsKey(e)){
                if( hashmap.get(e) == 0){
                    System.out.println("False");
                    break;
                }
                else{
                  hashmap.put(e,hashmap.get(e)-1);
                }
            }
            else{
                System.out.println("False");
                break;
            }
        }
        System.out.println(hashmap);
        System.out.println("Yes, Subset");
    }
}
