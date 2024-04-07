public interface DefaultMethodInterface {
    int add(int a, int b, int c);
    default void printSomething(){
        System.out.println("This is default method inside interface");
    }
}
