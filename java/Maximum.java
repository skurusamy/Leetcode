//Maximum in given window

import java.util.ArrayList;
import java.util.List;

public class Maximum {
    public static void main(String[] args) {
        int[] nums = {-4, 5, 4, -4, 4, 6, 7, 20};
        int w = 2;
        int j = 0;
        int i = 0;
        List<Integer> list = new ArrayList<>();
        int max_ele = Integer.MIN_VALUE;
        while(j < nums.length){
            max_ele = Math.max(max_ele,nums[j]);
            if(j - i == w-1){
                i ++;
                list.add(max_ele);
                max_ele = -Integer.MAX_VALUE;
                j = i;
            }
            else{
                j ++ ;
            }
            
        }
        System.out.println(list);
    }
}
