import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;

public class ListDemo {
    
    public  static void main(String[] args){
        Collection<String> collection = new ArrayList<>();
        collection.add("apple");
        collection.add("banana");

        List<String> lists = new ArrayList<>();
        lists.add("Tomato");
        lists.add("Onion");

       Collection<Integer> numbers = new ArrayList<>();
        for(int i = 0; i< 10;i++){
            numbers.add(10+i);
        }


        System.out.println(numbers);
        
        lists.set(1, "Brinjal");
        System.out.println(lists);

        for(Integer num: numbers){
            if(num% 2 == 0){
                System.out.print(num + " ");
            }
        }
        String[] string_arr = {"one","two","three","Four"};
        //List<String> listarray = Arrays.asList("one","two","three","Four");
        List<String> listarray = Arrays.asList(string_arr);
        System.out.println(listarray);

      for(String e: listarray){
        System.out.println(e);
      }

      lists.set(0, "q");
      lists.add("a");
      //Collections.sort(lists,Collections.reverseOrder());
      System.out.println(lists);
      
      
      
      Arrays.sort(string_arr,Collections.reverseOrder());
      for(String s : string_arr) System.out.println(s);

    }
}
