import java.util.Arrays;

public class isAnagram {
    public boolean isAnagram_(String s, String t) {
        char[] s_char = s.toCharArray();
        char[] t_char = t.toCharArray();
        Arrays.sort(s_char);
        
        String s_sort = new String(s_char);
        Arrays.sort(t_char);
        String t_sort = new String(t_char);
        System.out.println(String.valueOf(s_char));
        return s_sort.equals(t_sort);
    }

    public static void main(String[] args) {
        isAnagram an = new isAnagram();
        String s = "madam", t = "madassm";
        System.out.println(an.isAnagram_(s,t));
    }
}
