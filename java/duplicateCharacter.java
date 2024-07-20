import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;
import java.util.Map;

public class duplicateCharacter {
    public void findDuplicate(String s){
        char[] s_char = s.toCharArray();
        Set<Character> ans = new HashSet<>();
        Set<Character> char_set = new HashSet<>();
        for(char e: s_char){
            if(char_set.contains(e)){
                ans.add(e);
                char_set.remove(e);
            }
            else if(!ans.contains(e)){
                char_set.add(e);
            }
        }
        System.out.println(ans);
        System.out.println(char_set);
        System.out.println("Count of unique characters "+ char_set.size());
        System.out.println("Count of duplicates " + ans.size());
    }
    public void findDuplicate_hashmap(String s){
        Map<Character, Integer> hashmap = new HashMap<>();
        char[] s_char = s.toCharArray();
        Set<Character> ans = new HashSet<>();
        Set<Character> char_set = new HashSet<>();
        for(char e : s_char){
            hashmap.put(e, hashmap.getOrDefault(e,0)+1);
        }
        for(Map.Entry<Character, Integer> e : hashmap.entrySet()){
            if(e.getValue() != 1){
                ans.add(e.getKey());
            }
            else{
                char_set.add(e.getKey());
            }
        }
        System.out.println(ans);
        System.out.println(char_set);
        System.out.println("Count of unique characters "+ char_set.size());
        System.out.println("Count of duplicates " + ans.size());
    }
    public static void main(String[] args) {
        String s = "subhasreee";
        duplicateCharacter d = new duplicateCharacter();
        d.findDuplicate(s);
        d.findDuplicate_hashmap(s);

    }
}
