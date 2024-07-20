public class Palindrom {
    public static void main(String[] args) {
        String s = "madam";
        int i = 0, j = s.length() - 1;
        while(i<j){
            if(s.charAt(i) == s.charAt(j)){
                i += 1;
                j -= 1;
            }
            else{
                System.out.println("Not palindorme");
                break;
            }
        }
    }
}
