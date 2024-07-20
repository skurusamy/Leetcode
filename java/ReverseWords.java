import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ReverseWords {
    public static void main(String[] args) {
        String st = "I am fine";
        String[] st1 = st.split(" ");
        int i = 0, j = st1.length - 1;
        while(i<j){
            String tmp = st1[i];
            st1[i]  = st1[j];
            st1[j] = tmp;
            i ++;
            j --;
        }
        System.out.println(String.join(" ",st1));

        /*List<List<Integer>> list1 = new ArrayList<>();
        List<Integer> l = new ArrayList<>();
        l.add(1);
        l.add(2);
        l.add(3);
        list1.add(l);
        System.out.println(list1);*/

        int[][] arr = {{4,5},{1,3},{3,4},{2,3}};
        Arrays.sort(arr, (a,b) -> Integer.compare(a[0],b[0]));
        for(int[] row: arr){
            for(int e:row) System.out.println(e);
        } 
    }
}
