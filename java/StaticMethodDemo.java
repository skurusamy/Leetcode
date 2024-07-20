interface Shape{
    void shapeName();
    default void area(){
        System.out.println("This is Area Method");
    }
    static void Perimeter(){
        System.out.println("This is Perimeter");
    }
}

class Rectangle implements Shape{

    @Override
    public void shapeName() {
        System.out.println("This is Rectangle");
    }

    @Override
    public void area(){
        System.out.println("This is Rectangle area");
    }
    /*@Override
    public void Perimeter(){
        System.out.println("This is Rectangle Perimenter");
    }*/
    
}

public class StaticMethodDemo {
    
    public static void main(String[] args){
        Shape rectangle = new Rectangle();
        rectangle.area();
        rectangle.shapeName();

        Shape.Perimeter();
    }
}
