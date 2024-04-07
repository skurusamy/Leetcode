

import java.util.Vector;

public class Permutations {
    public static void main(String[] args) {
        String s = "Subha";
        Vector<String> ans = new Vector<>();
        for(int i = 0; i< s.length(); i++){
            for(int j = i+1 ; j <= s.length(); j++){
                ans.add(s.substring(i, j));
            }
            
        }
        System.out.println(ans);
    }
}
