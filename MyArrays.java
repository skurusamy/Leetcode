import java.util.Arrays;

public class MyArrays{
    public static void main (String[] args){
        int[] numbers = new int[10];
        for(int i =0;i< numbers.length-1;i++)
        {
            
            numbers[i] = i+1;
            System.out.print(i+1);
        }
        System.out.println(Arrays.toString(numbers));
        for(int a:numbers){
            System.out.println(a);
        }

    }

}