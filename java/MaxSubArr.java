public class MaxSubArr {
    public static void main(String[] args) {
        int[] arr = {1, 7, -2, -5, 10, -1};
        int max_sum =arr[0], curr_sum = 0;
        int  j = 0;
        while(j< arr.length){
            if(curr_sum < 0){
                curr_sum = 0;
            }
            curr_sum += arr[j];
            max_sum = Math.max(curr_sum,max_sum);
            j++;
        }
        System.out.println(max_sum);
        //System.out.println(ans);
    }
}
