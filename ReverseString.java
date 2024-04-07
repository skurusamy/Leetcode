public class ReverseString {
    public static void main(String[] args) {
        String s = "Subhasree";
        
        char[] s_char = s.toCharArray();
        int i = 0, j = s_char.length-1;
        while(i < j){
            char tmp = s_char[i];
            s_char[i] = s_char[j];
            s_char[j] = tmp;
            i += 1;
            j -= 1;
        }
        System.out.println(new String(s_char));
    }
}
