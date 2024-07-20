import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
class StreamFilterExample{
    public static void main(String[] args) {
        List<Employee> employeeList = new ArrayList<>();
        employeeList.add(new Employee(1, "abc", 100000));
        employeeList.add(new Employee(2, "cde", 50000));
        employeeList.add(new Employee(3, "tyu", 25000));

        for(Employee employee : employeeList){
            System.out.println(employee.getId() +" "+ employee.getName() +" "+ employee.getSalary());
        }
        List<Employee> filteredList = employeeList.stream().filter((employee)-> employee.getSalary() >= 50000 ).collect(Collectors.toList());
        for(Employee employee: filteredList){
            System.out.println(employee.getId() +" "+ employee.getName() +" "+ employee.getSalary());
        }

    }
   

}

class Employee{
    private int id;
    private String name;
    private int salary;
    public int getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    public int getSalary() {
        return salary;
    }
    public void setId(int id) {
        this.id = id;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setSalary(int salary) {
        this.salary = salary;
    }
    public Employee(int id, String name, int salary) {
        this.id = id;
        this.name = name;
        this.salary = salary;
    }
    
}