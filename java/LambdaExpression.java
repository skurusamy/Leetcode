interface Shape{
    void draw();
    default void print(){
        System.out.println("Printing");
    }
}




public class LambdaExpression {

    public static void printing(Shape shape){
        shape.draw();
    }
    public static void main(String[] args){
        Shape rectangle = () -> System.out.println("Rectangle");
        //rectangle.draw();

        printing(rectangle);
    }
    
}
