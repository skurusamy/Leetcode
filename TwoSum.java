import java.util.*;
class TwoSum {
    public int[] twoSum_usingArray(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++){
            for(int j= i+1; j < nums.length; j++){
                if(nums[i]+ nums[j] == target){
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{};
    }
    public int[] twoSum_hashMap(int[] nums, int target){
        Map<Integer,Integer> myHash = new HashMap<Integer,Integer>();
        for(int i= 0; i < nums.length;i++){
            myHash.put(nums[i], i);
        }
        for(int i = 0; i< nums.length;i++){
            if(myHash.containsKey(nums[i]) && myHash.get(nums[i]) != i){
                return new int[]{nums[i],i};
            }
        }
        return new int[]{};
    }
     public static void main(String[] args){
        int[] nums = {2,7,11,15};
        TwoSum obj = new TwoSum();
        int[] ans = obj.twoSum_usingArray(nums,9);
       
        for(int e : ans){
            System.out.print(e);
        }
        int[] ans_1 = obj.twoSum_usingArray(nums,9);
        for(int e1: ans_1){
            System.out.println(e1);
        }
    }
}