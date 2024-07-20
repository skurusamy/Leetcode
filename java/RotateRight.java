public class RotateRight {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5};
        int tmp = arr[arr.length-1];
        for(int i = arr.length-1; i>0; i--){
            arr[i] = arr[i-1];
        }
        arr[0] = tmp;
        for(int e: arr){
            System.out.println(e);
        }
    }
}
