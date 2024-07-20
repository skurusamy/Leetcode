import java.util.SortedMap;
import java.util.TreeMap;


public class CountEle{
    public static void main(String[] args) {
        int[] arr = {1,2,3,2,1,2,3,2,3};
        SortedMap<Integer, Integer> map = new TreeMap<>();
        for(int e : arr){
            map.put(e, map.getOrDefault(e,0)+1);
        }
        System.out.println(map);
        for(SortedMap.Entry<Integer,Integer> e : map.entrySet() ){
            System.out.println(e.getKey() + " "+ e.getValue());
        }
    }
}