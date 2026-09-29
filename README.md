# 🏢 Employee Management System

## 1. Project Overview
The **Employee Management System** is a console-based Python application designed to manage employee records. It serves as a practical implementation of fundamental programming concepts, showcasing how real-world entities and their relationships can be modeled using code. 

## 2. Objective
The primary objective of this project is to build an Employee Management System that demonstrates the basic Object-Oriented Programming (OOP) concepts I have studied in Python. It reinforces theoretical knowledge by applying it to a functional, menu-driven software program.

## 3. Features
The application provides a fully interactive console menu with the following capabilities:
- 👤 Create a Person
- 💼 Create an Employee
- 👔 Create a Manager
- 💻 Create a Developer
- 📋 Show details of Person, Employee, Manager, and Developer
- ✏️ Update an Employee
- ❌ Remove an Employee
- 🚪 Exit from the program
- 🖥️ Menu-driven console interface for easy navigation

## 4. OOP Concepts Used
This project extensively uses Object-Oriented Programming principles to maintain clean, modular, and reusable code:
- **Class and Object:** Blueprints for creating data entities.
- **`self` keyword:** To reference instance attributes and methods.
- **Constructor (`__init__`):** To initialize object states.
- **Destructor (`__del__`):** To handle basic resource cleanup.
- **Encapsulation & Private attributes:** Hiding sensitive data inside classes.
- **Getter and Setter methods:** For controlled access to private data.
- **Inheritance & Constructor inheritance:** Reusing code from parent classes.
- **`super()` method:** Calling parent class constructors and methods.
- **`issubclass()` function:** Checking class relationships dynamically.
- **Method Overriding & Polymorphism:** Tailoring inherited methods for specific child classes.
- **Function arguments & Default arguments:** Allowing multiple ways of creating Employee objects.

## 5. Technologies Used
- **Language:** Python 3.x
- **Core Python Basics Applied:**
  - Variables and Lists
  - Standard Input/Output (`input()`, `print()`)
  - Type casting (`int()`, `float()`)
  - Control Flow (`if`, `elif`, `else`)
  - Loops (`while`, `for`)
  - Functions, function arguments, and the `return` statement

## 6. Class Structure
The project models an organizational hierarchy using inheritance. 

**Hierarchy Flow:**
* `Person` → `Employee` → `Manager`
* `Person` → `Employee` → `Developer`

**Detailed Explanation:**
* **`Person` (Base Class):** Contains fundamental attributes like `name` and `age`.
* **`Employee` (Derived from Person):** Inherits from `Person`. It introduces employment-specific details. 
  * **Encapsulation:** The attributes `__employee_id` and `__salary` are made private (indicated by the double underscore). This protects sensitive data from being accidentally modified from outside the class.
  * **Getters and Setters:** Because the ID and salary are private, the class provides getter methods (like `get_salary()`) to read the values and setter methods (like `set_salary()`) to safely update them.
* **`Manager` (Derived from Employee):** Inherits all attributes from `Employee` and adds a unique `department` attribute.
* **`Developer` (Derived from Employee):** Inherits all attributes from `Employee` and adds a unique `programming_language` attribute.
* **Polymorphism and Method Overriding:** Every class has a method called `display()`. While the `Person` class has a basic `display()` method to show name and age, the child classes (`Employee`, `Manager`, `Developer`) **override** this method. When `display()` is called, the program dynamically executes the version of the method that belongs to that specific object, showing the correct, specialized details (like a Manager's department or a Developer's programming language).

## 7. How the Program Works
Upon running the script, the system initializes empty lists to store the created objects (`persons`, `employees`, `managers`, `developers`). An infinite `while` loop is used to continuously display the main menu. Based on the user's numeric input, `if/elif` statements route the program execution to specific functions (like `create_employee()` or `show_details()`). The loop breaks, and the program terminates gracefully only when the user selects the "Exit" option.
## 8. Menu Options

| Option | Action | Description |
| :--- | :--- | :--- |
| **1** | Create a Person | Prompts for basic details (name, age). |
| **2** | Create an Employee | Prompts for person details plus ID and Salary. |
| **3** | Create a Manager | Prompts for employee details plus Department. |
| **4** | Create a Developer | Prompts for employee details plus Programming Language. |
| **5** | Show Details | Opens a sub-menu to view specific lists of created records. |
| **6** | Update Employee | Modifies an existing employee's data based on their ID. |
| **7** | Remove Employee | Deletes an employee record based on their ID. |
| **8** | Exit | Ends the program. |

## 9. Example Console Output

```text
--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Create a Developer
5. Show Details
6. Update Employee
7. Remove Employee
8. Exit
Enter your choice: 2

Enter Employee Details
Enter Name: Jane Smith
Enter Age: 28
Enter Employee ID: E123
Enter Salary: 50000

Employee created with name: Jane Smith
Age: 28
Employee ID: E123
Salary: 50000.0
```

## 10. Project Structure
```text
Employee_Management_System/
│
├── employee_management.py   # Main Python source code file containing all classes and logic
└── README.md                # Project documentation
```

## 11. How to Run
To run this application on your local machine, ensure you have Python installed. Open your terminal or command prompt, navigate to the directory where the file is saved, and run the following command:

```bash
python employee_management.py
```

## 12. Learning Outcomes
Through building this project, I have gained practical experience in:
- Structuring a Python program using Object-Oriented design.
- Implementing data hiding (Encapsulation) and safe data modification.
- Extending functionality using Inheritance without rewriting code.
- Building a continuous, interactive console User Interface using loops and conditional logic.

## 13. Future Improvements
While the current system fulfills the core requirements, future versions could include:
- Implementing file handling to save records so data persists after closing the program.
- Adding a search feature to find employees by name rather than just by ID.
- Adding input validation logic to ensure users enter the correct data types (e.g., preventing letters from being entered as age) using conditional checks.

## 14. Author
**Manan Rami**  
B.Tech Computer Science and Engineering
