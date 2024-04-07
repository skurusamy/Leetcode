import java.util.Arrays;

public class ThreeSum {
    public static void main(String[] args) {
        int[] nums = {3,7,1,2,8,4,5};
        Arrays.sort(nums);
        int target = 10;
        for(int k = 0; k< nums.length; k++){
            int i = k+1, j = nums.length -1;
            while(i < j){
                int val = nums[i]+nums[j]+nums[k];
                if( val == target){
                    System.out.println(nums[i]+" "+nums[j]+" "+nums[k]);
                    i += 1;
                    j -= 1;
                    break;
                }
                else if(val  < target)
                {
                    i += 1;
                }
                else{
                    j -= 1;
                }
            }
            
        }
        System.out.println("No three sum");
    }
}
