import java.util.*;
public class StringCreation {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character,Integer> hashmap = new HashMap<>();
        char[] magazine_char = magazine.toCharArray();
        for(int i = 0; i< magazine_char.length; i++){
            hashmap.put(magazine_char[i],hashmap.getOrDefault(magazine_char[i],0) + 1);
        }
        for(int i = 0; i< ransomNote.length(); i++){
            char current_char = ransomNote.charAt(i);
            if(hashmap.containsKey(current_char) && hashmap.get(current_char) > 0){
                hashmap.put(current_char, hashmap.get(current_char)-1 );
            }
            else{
                return false;
            }
        }
        for(Map.Entry<Character, Integer> e : hashmap.entrySet()){
            System.out.println(e.getKey() +" " + e.getValue());
        }

        return true;

    }
    public static void main(String[] args) {
        StringCreation s = new StringCreation();
        boolean  ans = s.canConstruct("abcgt", "abvgggfy");
        System.out.println(ans);
    }
}
