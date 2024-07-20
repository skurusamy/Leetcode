public class ReArrange {
    public static void main(String[] args) {
        int[] arr = {10, -1, 20, 4, 5, -9, -6};
        int left = 0, right = arr.length-1;
        while(left < right){
            while(arr[left] < 0){
                left += 1;
            }
            while(arr[right] > 0){
                right -= 1;
            }
            if(left < right){
                int temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
            }
        }
        for(int e: arr){
            System.out.println(e);
        }
    }
}
