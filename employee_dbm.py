import sqlite3

# Connect to the database
conn = sqlite3.connect('employee.db')
c = conn.cursor()

# Create the employee table
c.execute('''CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                salary REAL NOT NULL
            )''')

# Function to add an employee
def add_employee():
    name = input("Enter the employee's name: ")
    position = input("Enter the employee's position: ")
    salary = float(input("Enter the employee's salary: "))

    c.execute('''INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)''',
              (name, position, salary))
    conn.commit()
    print("Employee added successfully!")

# Function to display all employees
def display_employees():
    c.execute('''SELECT * FROM employees''')
    employees = c.fetchall()

    if not employees:
        print("No employees found.")
    else:
        print("Employee List:")
        for employee in employees:
            print("ID: {employee[0]}, Name: {}, Position: {}, Salary: {}".format(employee[0],employee[1],employee[2],employee[3]))

# Function to update an employee's details
def update_employee():
    emp_id = int(input("Enter the ID of the employee to update: "))
    new_position = input("Enter the new position: ")
    new_salary = float(input("Enter the new salary: "))

    c.execute('''UPDATE employees SET position = ?, salary = ? WHERE id = ?''',
              (new_position, new_salary, emp_id))
    conn.commit()
    print("Employee details updated successfully!")

# Function to delete an employee
def delete_employee():
    emp_id = int(input("Enter the ID of the employee to delete: "))

    c.execute('''DELETE FROM employees WHERE id = ?''', (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")

# Main menu
def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee Details")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()


