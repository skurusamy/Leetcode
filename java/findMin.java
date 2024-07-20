public class findMin {
    public static void main(String[] args) {
        int[] arr = {9, 2, 3, 6};
        int ans = Integer.MAX_VALUE;
        for(int e : arr){
            if(e< ans)
                ans = e;
        }
        System.out.println(ans);
    }
}
