class Node {
    int data;
    Node next;

    public Node(int data){
        this.data = data;
        this.next = null;
    }
}

class LinkedListDemo {
    Node head;
    public LinkedListDemo(){
        this.head = null;
    }
    public void insertElement(int data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
        }
        else{
            Node curr = head;
            while(curr.next != null){
                curr = curr.next;
            }
            curr.next = newNode;
        }

    }
    public void display(){
        if(head == null){
            System.out.println("No Elements");
        }
        else{
            Node curr = head;
            while(curr != null){
                System.out.print(curr.data +" ");
                curr = curr.next;
            }
        
        }   
     }
    
}

class LinkedListApp{
    public static void main(String[] Args){
        LinkedListDemo ll = new LinkedListDemo();
        ll.insertElement(10);
        ll.insertElement(20);
        ll.display();
    }
}
