class Employee:
    def __init__(self,Employee_id=None,name=None,age=None,salary=None):
     self.__Employee_id = Employee_id
     self.name = name
     self.age = age
     self.__salary = salary

    def set_id(self,Employee_id):
        self.__Employee_id = Employee_id

    def get_id(self):
       return self.__Employee_id

    def set_salary(self,salary):
        self.__salary = salary

    def get_salary(self):  
        return self.__salary     

    def display(self):
        print(f"employee id is = {self.__Employee_id}")

    def __del__(self):
        print("destructor called")

class Manager(Employee):
    def __init__(self,Employee_id,name,age,salary,department):
        super().__init__(Employee_id,name,age,salary) 
        self.department = department

class Devloper(Employee):
    def __init__(self,Employee_id,name,age,salary,programming_language):   
        super().__init__(Employee_id,name,age,salary)
        self.programming_language = programming_language     

    def display(self):
        super().display()
        print(self.department)

print(f"devloper subclass of employee class = {issubclass(Devloper,Employee)}")
print(f"manager subclass of employee class = {issubclass(Manager,Employee)}")


person = None
employee = None
manager = None

while True:
    
    print("Choose an Operation: ")
    print("1. Create a Person: ")
    print("2. Create a Employee: ")
    print("3. Create a Manager: ")
    print("4. Show Details: ")
    print("5. Exit")

    choice = int(input("Enter Your Choice Number"))

    if choice == 1:

        name = input("Enter your name")
        age = int(input("Enter your age"))

        person = Employee(name=name,age=age)
        print(f"Your name is {name} and age is {age}")

    elif choice == 2:
        Employee_id = int(input("Enter your employee_id"))
        name = input("Enter your name")
        age = int(input("Enter your age")) 
        salary = int(input("Enter your salary"))

        employee = Employee(Employee_id,name,age,salary)
        print(f"create employee employee_id is {Employee_id}")
        print(f"name is {name} ")
        print(f"age is {age} ")
        print(f"salary is {salary} ")

    elif choice == 3:
           Employee_id = int(input("Enter your employee_id"))
           name = input("Enter your name")
           age = int(input("Enter your age"))
           salary = int(input("Enter your salary"))
           department = input("Enter your department")

           manager = Manager(Employee_id,name,age,salary,department)
           print(f"create manager employee_id is {Employee_id} ")
           print(f"name is {name}")
           print(f"age is {age}") 
           print(f"salary is {salary}")
           print(f"department: {department}")

    elif choice == 4:
        print("Choose details to show: ")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        ch = int(input("Enter your number"))

        if ch == 1:
            if person is None:
                print("No Manager created")
                print("---------- Person ----------")
                
            else:
                    person.display()     

        elif ch == 2:
            print("---------- Employee ----------") 
            employee.display()

        elif ch == 3:
                print("---------- Manager ----------")
                manager.display()    
              
    elif choice == 5:
           print("Exiting the system All resources have been freed.")
           break
    else:
        print("Invalid choice")               
                      


