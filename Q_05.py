
# 20099_Maniruzzaman_Md_lab3
# Week_03/lab_03/Q_05
# Question: program for employee management according to ID, Depertment, age ...


def info(employees):  # define function and import employee info for store
    name = input("\nEnter employee's name\t: ").upper()
    id = input("Enter employee's ID\t: ")
    department = input("Enter department number\t: ").upper()
    age = input("Enter employee's age\t: ")

    employee = [name, id, department, age]
    employees.append(employee)
    print("Employee information entered successfully.")

def display_all_employees(employees):    # define function for display all stored employee
    print("\nAll Employee's Information:")
    for employee in employees:
        print("\nName\t\t:", employee[0])
        print("ID\t\t:", employee[1])
        print("Department\t:", employee[2])
        print("Age\t\t:", employee[3])
        print("-" * 35)

def find_by_name(employees):              # define function for display employee details by name
    nm_find = input("\nEnter name of the employee: ").upper()
    fnd_employee = [employee for employee in employees if employee[0] == nm_find]

    if fnd_employee:
        print("\nFound Employees information:")
        for employee in fnd_employee:
            print("Name\t\t:", employee[0])
            print("ID\t\t:", employee[1])
            print("Department\t:", employee[2])
            print("Age\t\t:", employee[3])
            print("-" * 35)
    else:
        print("\nNo employees found with the given name.")
        add_emp = input("Want to add this employee? (yes/no): ")
        if add_emp.lower() == "yes":
            info(employees)

def show_by_age(employees):                 # define function to display employee list by age
    sorted_emp_list = sorted(employees, key=lambda x: int(x[3]))  # Sort by age
    print("\nEmployee's Information in Chronological Order by Age:")
    for employee in sorted_emp_list:
        print("Name\t\t:", employee[0])
        print("ID\t\t:", employee[1])
        print("Department\t:", employee[2])
        print("Age\t\t:", employee[3])
        print("-" * 35)

def remove_by_id(employees):                 # define function for remove employee by ID number from storage
    id_remove = input("\nEnter employee ID number to remove: ")
    removed = False

    for employee in employees:
        if employee[1] == id_remove:
            employees.remove(employee)
            removed = True
            print("\nEmployee removed successfully.")
            break

    if not removed:
        print("\nNo employee found with the given ID.")

def main():                                 # main function define to main menu and call other function as required
    employees = []

    while True:
        print("\n========= Menu ==========")
        print("1. Enter a new employee's information")
        print("2. Display all employee's information")
        print("3. Find employee's information by name")
        print("4. Display all employees' information in chronological order by age")
        print("5. Remove the employee by ID")
        print("6. Quit")

        choice = input("\nEnter your choice (1-6): ")
        # function call
        if choice == "1":
            info(employees)
        elif choice == "2":
            display_all_employees(employees)
        elif choice == "3":
            find_by_name(employees)
        elif choice == "4":
            show_by_age(employees)
        elif choice == "5":
            remove_by_id(employees)
        elif choice == "6":
            exit_opt = input("Are you want to exit? (yes/no): ")
            if exit_opt.lower() == "yes":
                print("Exiting the program. Goodbye!")
                break
        else:
            print("Invalid selection. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
