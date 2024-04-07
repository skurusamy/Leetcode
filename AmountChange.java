import java.util.Vector;

public class AmountChange {
    public static void main(String[] args) {
        
        int amount = 10;
        int[] coins = {1,2,3};
        Vector<Integer> ans = new Vector<>();
        for(int i = coins.length-1; i>=0;i--){
            while(amount > 0){
                ans.add(coins[i]);
                amount -= coins[i];
                if(amount == 0){
                    break;
                }
            }
        }
        for(int e :ans){
            System.out.println(e);
        }
    }
}
