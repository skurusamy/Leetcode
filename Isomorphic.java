import java.util.HashMap;
import java.util.Map;

public class Isomorphic {
    public String findPattern(String s){
        Map<Character, Integer> map = new HashMap<>();
        for(int i = 0; i< s.length(); i ++){
            map.put(s.charAt(i),i);
        }
        String pattern = "";
        for(int i = 0; i< s.length(); i ++){
            pattern += map.get(s.charAt(i));
        }
        System.out.println(pattern);
        return pattern;
    }
    public boolean isIsomorphic(String s, String t) {
        String pattern1 = findPattern(s);
        String pattern2 = findPattern(t);
        System.out.println(pattern1 + " "+ pattern2);
        return pattern1.equals(pattern2);
    }
    public static void main(String[] args) {
        String s = "add", t = "eggh";
        Isomorphic is = new Isomorphic();
        boolean ans = is.isIsomorphic(s, t);
        System.out.println(ans);
    }
}
