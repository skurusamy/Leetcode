import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class Leetcode2462{
    public static void main(String[] args) {
        int[] costs = {17,12,10,2,7,2,11,20,8};
        int k = 3, candidates = 4;
        PriorityQueue<Integer> pq1 = new PriorityQueue<>();
        long final_cost = 0;
        List<Integer> costs_list = new ArrayList<>();
        for(int e: costs) costs_list.add(e);
        while(k > 0){
            if(costs_list.size() < candidates){
                pq1.clear();
                for(int e : costs_list) pq1.add(e);
            }
            else{
                for(int i = 0; i < candidates; i++){
                if(!pq1.contains(costs_list.get(i)) ){
                    pq1.add(costs_list.get(i));
                    }
                } 
            
                for(int i = costs_list.size() - 1 ;i > costs_list.size() - candidates; i--){
                if(!pq1.contains(costs_list.get(i))){
                    pq1.add(costs_list.get(i));
                    }
                } 
            } 
            
            int min_val = pq1.poll();
            final_cost += min_val;
            System.out.println(costs_list);
            costs_list.remove(Integer.valueOf(min_val));
            System.out.println("After remove:" +min_val+" "+ costs_list);
            k -= 1;
        }
        System.out.println(final_cost);
    }
}