
class ThreadDemo implements Runnable{

    @Override
    public void run() {
        System.out.println("Runnable method");
    }

}


public class RunnableDemo {


    public static void main(String[] args){

        Thread thread = new Thread(new ThreadDemo());
        thread.start();

    }
    
    
}
