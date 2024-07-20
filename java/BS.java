public class BS {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,5,6,7,8};
        int ele = 7;
        int left = 0, right = arr.length;
        while(left < right){
            int mid = ((left+right)/2);
            if(arr[mid] == ele){
                System.out.println("Element found");
                break;
            }
            else if(arr[mid]> ele){
                right = mid -1;
            }
            else{
                left = mid + 1;
            }
        }
    }
}
