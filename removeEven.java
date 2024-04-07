import java.util.ArrayList;
import java.util.List;

public class removeEven {
    public void removeEvenInt(int[] arr){
        List<Integer> ans = new ArrayList<>();
        for(int i = 0;i<arr.length;i++){
            if(arr[i]%2 != 0){
                ans.add(arr[i]);
            }
        }
        System.out.println(ans);
    }
    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 5, 10, 6, 3};
        int left = 0, right = arr.length -1;
        while (left < right){
            while (left < arr.length -1 && arr[left] % 2 == 1){ // left is odd
                left += 1;
            }
            while(right >= 0 && arr[right] % 2 == 0){
                right -= 1;
            }
            if(left < right){
                int tmp = arr[left];
                arr[left] = arr[right];
                arr[right] = tmp;
                left += 1;
                right -= 1;
            }
        }
        for(int e: arr){
            System.out.println(e);
        }
    }
}
