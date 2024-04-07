public class SecondMax{
    public static void main(String[] args) {
        int[] arr = {9,2,3,6};
        int first_max = Integer.MIN_VALUE, second_max = Integer.MIN_VALUE;
        for(int e : arr){
            if(e > first_max){
                first_max = e;
            }
        }
        System.out.println(first_max);
        for(int i =0;i< arr.length;i++){
            if(arr[i] > second_max && arr[i] != first_max){
                second_max = arr[i];
            }
        }
        System.out.println(second_max);
    }
}
