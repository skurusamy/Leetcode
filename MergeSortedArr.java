public class MergeSortedArr {
    public static void main(String[] args) {
        int[] arr1 = {1, 3, 4, 5};
        int[] arr2 = {2, 6, 7, 8};
        int[] result = new int[arr1.length+arr2.length];
        int i = 0, j= 0, k = 0;
        while(i< arr1.length && j < arr2.length){
            if(arr1[i] < arr2[j]){
                result[k] = arr1[i];
                i += 1;
            }
            else{
                result[k] = arr2[j];
                j += 1;
            }
            k += 1;
        }
        while(i< arr1.length){
            result[k] = arr1[i];
            i += 1;
            k += 1;
        }
        while(j< arr2.length){
            result[k] = arr2[j];
            j += 1;
            k += 1;
        }
        for(int e : result){
            System.out.print(e+" ");
        }
    }
}
