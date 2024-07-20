import java.util.*;
public class BalanceParanthesis {
    public boolean validateParanthesis(String inpString){
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < inpString.length(); i++ ){
            if(inpString.charAt(i) == '('){
                stack.push(inpString.charAt(i));
            }
            else{
                char curr = stack.pop();
                if(curr == ')'){
                    return false;
                }
            }
        }
        return stack.empty();
    }
    public static void main(String[] args){
        BalanceParanthesis bp = new BalanceParanthesis();
        String input = "((()))";
        boolean ans = bp.validateParanthesis(input);
        System.out.println(ans);
    }
}
