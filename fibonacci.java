public class fibonacci{
    public static void main(String[] args) {
        int n = 5;
        int first = 0;
        int second = 1;
        int i = 2;
        System.out.println(first);
        System.out.println(second);
        
        while(i<=n){
            int curr = first + second;
            first = second;
            second = curr;
            System.out.println(curr);
            i++;
        }
    }
}