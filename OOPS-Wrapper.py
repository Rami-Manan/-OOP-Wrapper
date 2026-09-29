# -------------------- Person Class --------------------

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        pass


# -------------------- Employee Class --------------------

class Employee(Person):

    def __init__(self, name, age, employee_id=None, salary=None):
        super().__init__(name, age)

        self.__employee_id = employee_id
        self.__salary = salary

    # Getter for Employee ID
    def get_employee_id(self):
        return self.__employee_id

    # Setter for Employee ID
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    # Getter for Salary
    def get_salary(self):
        return self.__salary

    # Setter for Salary
    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        pass


# -------------------- Manager Class --------------------

class Manager(Employee):

    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)

        self.department = department

    # Method Overriding
    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Department:", self.department)

    def __del__(self):
        pass


# -------------------- Developer Class --------------------

class Developer(Employee):

    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)

        self.programming_language = programming_language

    # Method Overriding
    def display(self):
        print("\nDeveloper Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.get_salary())
        print("Programming Language:", self.programming_language)

    def __del__(self):
        pass


# -------------------- Lists --------------------

persons = []
employees = []
managers = []
developers = []


# -------------------- Create Person --------------------

def create_person():

    print("\nEnter Person Details")

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    person = Person(name, age)

    persons.append(person)

    print("\nPerson created with name:", name, "and age:", age)


# -------------------- Create Employee --------------------

def create_employee():

    print("\nEnter Employee Details")

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))

    employee = Employee(name, age, employee_id, salary)

    employees.append(employee)

    print("\nEmployee created with name:", name)
    print("Age:", age)
    print("Employee ID:", employee_id)
    print("Salary:", salary)


# -------------------- Create Manager --------------------

def create_manager():

    print("\nEnter Manager Details")

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    manager = Manager(
        name,
        age,
        employee_id,
        salary,
        department
    )

    managers.append(manager)

    print("\nManager created with name:", name)
    print("Age:", age)
    print("Employee ID:", employee_id)
    print("Salary:", salary)
    print("Department:", department)


# -------------------- Create Developer --------------------

def create_developer():

    print("\nEnter Developer Details")

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    programming_language = input("Enter Programming Language: ")

    developer = Developer(
        name,
        age,
        employee_id,
        salary,
        programming_language
    )

    developers.append(developer)

    print("\nDeveloper created with name:", name)
    print("Age:", age)
    print("Employee ID:", employee_id)
    print("Salary:", salary)
    print("Programming Language:", programming_language)


# -------------------- Show Person Details --------------------

def show_person_details():

    if len(persons) == 0:
        print("\nNo Person details available.")
    else:
        for person in persons:
            person.display()


# -------------------- Show Employee Details --------------------

def show_employee_details():

    if len(employees) == 0:
        print("\nNo Employee details available.")
    else:
        for employee in employees:
            employee.display()


# -------------------- Show Manager Details --------------------

def show_manager_details():

    if issubclass(Manager, Employee):

        if len(managers) == 0:
            print("\nNo Manager details available.")
        else:
            for manager in managers:
                manager.display()


# -------------------- Show Developer Details --------------------

def show_developer_details():

    if issubclass(Developer, Employee):

        if len(developers) == 0:
            print("\nNo Developer details available.")
        else:
            for developer in developers:
                developer.display()


# -------------------- Show Details Menu --------------------

def show_details():

    print("\nChoose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    print("4. Developer")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        show_person_details()

    elif choice == 2:

        show_employee_details()

    elif choice == 3:

        show_manager_details()

    elif choice == 4:

        show_developer_details()

    else:

        print("\nInvalid choice.")


# -------------------- Update Employee --------------------

def update_employee():

    if len(employees) == 0:
        print("\nNo Employee available.")
        return

    employee_id = input("\nEnter Employee ID to update: ")

    found = False

    for employee in employees:

        if employee.get_employee_id() == employee_id:

            print("\nEmployee found.")

            new_name = input("Enter New Name: ")
            new_age = int(input("Enter New Age: "))
            new_salary = float(input("Enter New Salary: "))

            employee.name = new_name
            employee.age = new_age
            employee.set_salary(new_salary)

            print("\nEmployee updated successfully.")

            found = True

    if not found:
        print("\nEmployee not found.")


# -------------------- Remove Employee --------------------

def remove_employee():

    if len(employees) == 0:
        print("\nNo Employee available.")
        return

    employee_id = input("\nEnter Employee ID to remove: ")

    found = False

    for employee in employees:

        if employee.get_employee_id() == employee_id:

            employees.remove(employee)

            print("\nEmployee removed successfully.")

            found = True
            break

    if not found:
        print("\nEmployee not found.")


# -------------------- Main Menu --------------------

while True:

    print("\n--- Python OOP Project: Employee Management System ---")

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Create a Developer")
    print("5. Show Details")
    print("6. Update Employee")
    print("7. Remove Employee")
    print("8. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        create_person()

    elif choice == 2:

        create_employee()

    elif choice == 3:

        create_manager()

    elif choice == 4:

        create_developer()

    elif choice == 5:

        show_details()

    elif choice == 6:

        update_employee()

    elif choice == 7:

        remove_employee()

    elif choice == 8:

        print("\nThank you for using Employee Management System.")
        break

    else:

        print("\nInvalid choice. Please enter a number from 1 to 8.")
