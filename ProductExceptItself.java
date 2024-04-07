public class ProductExceptItself {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4};
        int[] left_arr = new int[arr.length];
        int[] right_arr = new int[arr.length];
        left_arr[0] = 1;
        right_arr[arr.length-1] = 1;
        for(int i = 1;i< arr.length;i++){
            left_arr[i] = arr[i-1] * left_arr[i-1];
        }
        for(int j = arr.length-2;j>=0;j --){
            right_arr[j] = right_arr[j+1] * arr[j+1];
        }
        for(int i = 0; i< arr.length;i++){
            System.out.println(left_arr[i]+" "+right_arr[i]);
            arr[i] = left_arr[i] * right_arr[i];
        }
        for(int e: arr){
            System.out.println(e);
        }
    }
}
