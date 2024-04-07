import java.util.Scanner;

class BubbleSort{
    public static void main(String[] args) {
            try (// Reading the input 
            Scanner in = new Scanner(System.in)) {
                System.out.println("Enter the number of elements in the array: ");
                int n = in.nextInt();
                int[] arr = new int[n];
                System.out.println("Enter the elements:");
                for(int i = 0;i<arr.length; i++){
                    arr[i] = in.nextInt();
                }

                //Printing all the elements in an array
                System.out.print("The elements in the array are ");
                for(int i= 0;i<arr.length;i++){
                    System.out.print(arr[i]+" ");
                }
                System.out.println("\nThe composite numbers are:");

                //Calculating composite number
                for(int i= 0;i<arr.length;i++){
                    int num = arr[i];
                    if(num <= 1)
                        continue;
                    if(num<=3)
                        continue;
                    if (num % 2 == 0 || num % 3 == 0){
                        System.out.println(num);
                    }
                    for (int j = 5; j * j <= num; j = j + 6){
                        if(num%j == 0 || num % (j+2) == 0){
                            System.out.println(num);
                            break;
                        }
                    }
                }
            }
            
        }

}
