# Employee Details

A simple **Employee Management System** built using **Python** and **Object-Oriented Programming (OOP)**.

This project demonstrates important OOP concepts such as inheritance, encapsulation, constructors, destructors, getters, setters, method overriding, `super()`, and `issubclass()`.

---

# 🚀 Features

- Create a Person
- Create an Employee
- Create a Manager
- Create a Developer
- Show Details
- Inheritance
- Encapsulation
- Constructor
- Destructor
- Getter and Setter
- Method Overriding
- `super()`
- `issubclass()`
- Menu-driven program

---

# 📚 Classes

## 👤 Person

The `Person` class is used to store basic personal information.

```python
class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age
```

It contains:

- Name
- Age

---

## 👨‍💼 Employee

The `Employee` class contains employee-related information.

```python
class Employee(Person):
```

It contains:

- Employee ID
- Name
- Age
- Salary

Example:

```python
class Employee(Person):

    def __init__(self, Employee_id=None, name=None, age=None, salary=None):
        super().__init__(name, age)
        self.__Employee_id = Employee_id
        self.__salary = salary
```

---

## 👨‍💼 Manager

The `Manager` class inherits from the `Employee` class.

```python
class Manager(Employee):
```

It contains:

- Employee ID
- Name
- Age
- Salary
- Department

Example:

```python
class Manager(Employee):

    def __init__(self, Employee_id, name, age, salary, department):
        super().__init__(Employee_id, name, age, salary)
        self.department = department
```

---

## 👨‍💻 Developer

The `Developer` class inherits from the `Employee` class.

```python
class Developer(Employee):
```

It contains:

- Employee ID
- Name
- Age
- Salary
- Programming Language

Example:

```python
class Developer(Employee):

    def __init__(self, Employee_id, name, age, salary, programming_language):
        super().__init__(Employee_id, name, age, salary)
        self.programming_language = programming_language
```

> **Note:** If your Python file uses `Devloper` instead of `Developer`, keep the same spelling in the README and source code. The standard English spelling is `Developer`.

---

# 🧠 OOP Concepts

## 1. Inheritance

Inheritance allows one class to inherit properties and methods from another class.

### Manager

```python
class Manager(Employee):
    pass
```

### Developer

```python
class Developer(Employee):
    pass
```

Both `Manager` and `Developer` inherit from `Employee`.

---

## 2. Encapsulation

Encapsulation is used to restrict direct access to certain attributes.

Employee ID and salary are stored as private attributes:

```python
self.__Employee_id
self.__salary
```

The double underscore `__` is used to make these attributes private.

---

## 3. Getter and Setter

Getter and setter methods are used to access and modify private attributes.

### Employee ID Getter

```python
def get_id(self):
    return self.__Employee_id
```

### Employee ID Setter

```python
def set_id(self, Employee_id):
    self.__Employee_id = Employee_id
```

### Salary Getter

```python
def get_salary(self):
    return self.__salary
```

### Salary Setter

```python
def set_salary(self, salary):
    self.__salary = salary
```

---

## 4. Constructor

The constructor is automatically called when an object is created.

```python
def __init__(self, Employee_id=None, name=None, age=None, salary=None):
    self.__Employee_id = Employee_id
    self.name = name
    self.age = age
    self.__salary = salary
```

The constructor initializes the object attributes.

---

## 5. Destructor

The destructor is called when an object is destroyed.

```python
def __del__(self):
    print("Destructor called")
```

---

## 6. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method already defined in the parent class.

Example:

```python
def display(self):
    super().display()
    print(self.department)
```

The child class can extend or modify the behavior of the parent class.

---

## 7. `super()`

The `super()` function is used to call methods from the parent class.

Example:

```python
super().__init__(Employee_id, name, age, salary)
```

This calls the constructor of the `Employee` parent class.

---

## 8. `issubclass()`

The `issubclass()` function checks whether a class is derived from another class.

Example:

```python
issubclass(Developer, Employee)
issubclass(Manager, Employee)
```

Output:

```text
Developer subclass of Employee class = True
Manager subclass of Employee class = True
```

---

# 📋 Main Menu

The program provides a menu-driven interface:

```text
Choose an Operation:

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit
```

---

# 👤 Create a Person

The user can create a person by entering:

```text
Name
Age
```

Example:

```text
Enter Name: Rahul
Enter Age: 25
```

---

# 👨‍💼 Create an Employee

The user can create an employee by entering:

```text
Employee ID
Name
Age
Salary
```

Example:

```text
Enter Employee ID: 101
Enter Name: Rahul
Enter Age: 25
Enter Salary: 30000
```

---

# 👨‍💼 Create a Manager

The user can create a manager by entering:

```text
Employee ID
Name
Age
Salary
Department
```

Example:

```text
Enter Employee ID: 102
Enter Name: Amit
Enter Age: 30
Enter Salary: 50000
Enter Department: IT
```

---

# 👨‍💻 Create a Developer

The user can create a developer by entering:

```text
Employee ID
Name
Age
Salary
Programming Language
```

Example:

```text
Enter Employee ID: 103
Enter Name: Jay
Enter Age: 24
Enter Salary: 40000
Enter Programming Language: Python
```

---

# 📄 Show Details

The program allows the user to display information.

```text
Choose details to show:

1. Person
2. Employee
3. Manager
4. Developer
```

The selected object's details are displayed.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python 3** | Programming Language |
| **OOP** | Object-Oriented Programming |
| **Classes** | Creating objects and organizing code |
| **Inheritance** | Reusing parent class functionality |
| **Encapsulation** | Protecting private attributes |
| **Constructor** | Initializing objects |
| **Destructor** | Destroying objects |
| **Getter** | Accessing private attributes |
| **Setter** | Modifying private attributes |
| **Method Overriding** | Changing inherited behavior |
| **`super()`** | Calling parent class methods |
| **`issubclass()`** | Checking class inheritance |
| **Loops** | Menu control |
| **Conditional Statements** | Handling user choices |

---

# 📂 Project Structure

```text
Employee-Management-System/
│
├── main.py
├── output.png
└── README.md
```

---

# ▶️ How to Run

## Step 1: Install Python

Make sure Python 3 is installed.

Check your Python version:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## Step 2: Clone the Repository

```bash
git clone <your-repository-url>
```

---

## Step 3: Open the Project Directory

```bash
cd Employee-Management-System
```

---

## Step 4: Run the Program

```bash
python main.py
```

or:

```bash
python3 main.py
```

---

# 🧪 Sample Output

```text
Choose an Operation:

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice: 3

Enter Employee ID: 102
Enter Name: Amit
Enter Age: 30
Enter Salary: 50000
Enter Department: IT

Manager Details:
Employee ID: 102
Name: Amit
Age: 30
Salary: 50000
Department: IT
```

---

# 📸 Program Output

The following image shows the program output:

![Program Output](output.png)

---

# 🎯 Learning Objectives

This project helps demonstrate the following Python and OOP concepts:

- Classes and Objects
- Inheritance
- Encapsulation
- Constructors
- Destructors
- Getters
- Setters
- Method Overriding
- `super()`
- `issubclass()`
- Private Attributes
- Menu-driven Programming
- Conditional Statements
- Loops

---

# 💡 Future Improvements

Possible improvements for this project include:

- Add database support
- Store multiple employees
- Search employees by ID
- Update employee details
- Delete employee records
- Save employee information to a file
- Add CSV file support
- Add exception handling
- Add a graphical user interface
- Add login and authentication

---

# ⚠️ Note

If the Python source code currently uses:

```python
class Devloper(Employee):
```

you can keep it as it is.

However, the conventional spelling is:

```python
class Developer(Employee):
```

---

# 👨‍💻 Author

**Employee Details / Employee Management System**

A Python project created to demonstrate Object-Oriented Programming concepts and basic employee management.

---

# 📜 License

This project is created for educational and learning purposes.
