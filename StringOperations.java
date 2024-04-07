import java.util.Arrays;

public class StringOperations {
    public static void main(String[] args) {
       //To sort a string 
        String s = "IamaString";
        String newString =s.chars().sorted().collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append).toString();
        System.out.println(newString);

        char[] s_char = s.toCharArray();
        Arrays.sort(s_char);
        System.out.println(new String(s_char));

        //Working with String Buffer
        StringBuffer sb = new StringBuffer();
        sb.append("a");
        sb.append(" newString");
        
        System.out.println(sb);
        System.out.println(sb.capacity());
        System.out.println(sb.length());
        System.out.println(sb.substring(6));

    }
}
