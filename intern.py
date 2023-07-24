import tkinter as tk

# Function to handle customer login
def customer_login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the username and password are valid for a customer
    if username == "rajat" and password == "2003":
        # If valid, show the menu screen
        show_menu_screen()
    else:
        # If invalid, show an error message
        error_label.config(text="Invalid username or password")

# Function to handle employee login
def employee_login():
    username = emp_username_entry.get()
    password = emp_password_entry.get()
    
    # Check if the username and password are valid for an employee
    if username == "emp" and password == "password":
        # If valid, show the employee salary screen
        show_employee_salary_screen()
    else:
        # If invalid, show an error message
        error_label.config(text="Invalid username or password")

# Function to show the menu screen
def show_menu_screen():
    # Hide the login screen
    login_frame.pack_forget()
    emp_login_frame.pack_forget()
    
    # Create and display the menu screen
    menu_frame.pack()

# Function to show the employee salary screen
def show_employee_salary_screen():
    # Hide the login screen
    login_frame.pack_forget()
    emp_login_frame.pack_forget()
    
    # Create and display the employee salary screen
    salary_frame.pack()
    salary_label.config(text="Salary: ₹5000")  # Replace with the actual salary

# Function to handle order button click
def place_order():
    selected_items = []
    total_price = 0
    
    # Get the selected items and their quantities
    for item, var in menu_vars.items():
        if var.get() == 1:
            quantity = quantity_vars[item].get()
            selected_items.append((item, quantity))
            total_price += menu_items[item] * quantity
    
    # Create and display the order summary screen
    order_summary.config(text="Order Summary\n")
    for item, quantity in selected_items:
        order_summary.config(text=order_summary.cget("text") + f"{item} - Quantity: {quantity}\n")
    order_summary.config(text=order_summary.cget("text") + f"Total Price: ${total_price:.2f}")
    order_summary_frame.pack()

# Function to handle confirm button click
def confirm_order():
    # Hide the order summary screen
    order_summary_frame.pack_forget()
    
    # Show the confirmation message
    confirmation_label.config(text="Order confirmed! Enjoy your meal.")
    confirmation_frame.pack()

# Create the main window
window = tk.Tk()
window.title("Restaurant Management System")

# Create the login screen
login_frame = tk.Frame(window)

username_label = tk.Label(login_frame, text="Username:")
username_label.pack()

username_entry = tk.Entry(login_frame)
username_entry.pack()

password_label = tk.Label(login_frame, text="Password:")
password_label.pack()

password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

customer_login_button = tk.Button(login_frame, text="Customer Login", command=customer_login)
customer_login_button.pack()

error_label = tk.Label(login_frame, fg="red")
error_label.pack()

# Initially hide the login screen
login_frame.pack()

# Create the employee login screen
emp_login_frame = tk.Frame(window)

emp_username_label = tk.Label(emp_login_frame, text="Employee Username:")
emp_username_label.pack()

emp_username_entry = tk.Entry(emp_login_frame)
emp_username_entry.pack()

emp_password_label = tk.Label(emp_login_frame, text="Employee Password:")
emp_password_label.pack()

emp_password_entry = tk.Entry(emp_login_frame, show="*")
emp_password_entry.pack()

employee_login_button = tk.Button(emp_login_frame, text="Employee Login", command=employee_login)
employee_login_button.pack()

# Create the menu screen
menu_frame = tk.Frame(window)

menu_label = tk.Label(menu_frame, text="Menu")
menu_label.pack()

# Sample menu items and prices
menu_items = {
    "Cheeseburger": 9.99,
    "French Fries": 4.99,
    "Caesar Salad": 8.99,
    "Pizza": 12.99,
    "Ice Cream": 3.99,
}

menu_vars = {}  # Dictionary to store the checkbox variables
quantity_vars = {}  # Dictionary to store the quantity entry variables

for item, price in menu_items.items():
    var = tk.IntVar()
    menu_vars[item] = var
    
    checkbox = tk.Checkbutton(menu_frame, text=f"{item} - ${price:.2f}", variable=var)
    checkbox.pack(anchor=tk.W)
    
    quantity_label = tk.Label(menu_frame, text="Quantity:")
    quantity_label.pack()
    
    quantity_var = tk.IntVar()
    quantity_vars[item] = quantity_var
    
    quantity_entry = tk.Entry(menu_frame, textvariable=quantity_var)
    quantity_entry.pack()

# Order button
order_button = tk.Button(menu_frame, text="Order", command=place_order)
order_button.pack()

# Initially hide the menu screen
menu_frame.pack_forget()

# Create the order summary screen
order_summary_frame = tk.Frame(window)
order_summary = tk.Label(order_summary_frame, text="")
order_summary.pack()

# Confirm button
confirm_button = tk.Button(order_summary_frame, text="Confirm", command=confirm_order)
confirm_button.pack()

# Initially hide the order summary screen
order_summary_frame.pack_forget()

# Create the employee salary screen
salary_frame = tk.Frame(window)

salary_label = tk.Label(salary_frame, text="")
salary_label.pack()

# Initially hide the employee salary screen
salary_frame.pack_forget()

# Create the confirmation screen
confirmation_frame = tk.Frame(window)
confirmation_label = tk.Label(confirmation_frame, text="")
confirmation_label.pack()

# Initially hide the confirmation screen
confirmation_frame.pack_forget()

# Start the application
window.mainloop()