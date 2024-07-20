public class DefaultMethodDemo implements DefaultMethodInterface {
    public static void main(String[] args){
        DefaultMethodDemo d = new DefaultMethodDemo();
        d.printSomething();
    }
    @Override
    public int add(int a, int b, int c) {
      // TODO Auto-generated method stub
      return a+b+c;
    }
    
}
