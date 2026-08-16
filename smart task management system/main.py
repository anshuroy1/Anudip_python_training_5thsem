from datetime import datetime


# ============================================================
# TASK CLASS
# ============================================================

# Class to represent a single task
class Task:

    # Initialize task details
    def __init__(self, task_id, title, description, priority, due_date):

        self.task_id = task_id          # Unique ID of the task
        self.title = title              # Task title
        self.description = description  # Task description
        self.priority = priority        # Task priority
        self.due_date = due_date        # Task deadline
        self.status = "Pending"         # Default task status


# ============================================================
# TASK LIST
# ============================================================

# List to store all task objects
tasks = []


# ============================================================
# TASK ID VALIDATION
# ============================================================

# Function to get and validate Task ID
def get_task_id():

    while True:

        try:
            # Take Task ID from the user
            task_id = int(input("Enter Task ID: "))

            # Task ID must be greater than zero
            if task_id <= 0:
                print("Task ID must be greater than 0.")
                continue

            # Check whether Task ID already exists
            for task in tasks:

                if task.task_id == task_id:
                    print("Task ID already exists! Enter a different ID.")
                    break

            else:
                # Return ID if it is unique
                return task_id

        except ValueError:
            # Handle non-numeric input
            print("Invalid input! Task ID must be a number.")


# ============================================================
# TITLE VALIDATION
# ============================================================

# Function to get and validate task title
def get_title():

    while True:

        # Take task title from the user
        title = input("Enter Task Title: ").strip()

        # Title cannot be empty
        if title == "":
            print("Task title cannot be empty.")

        # Title cannot contain only numbers
        elif title.isdigit():
            print("Task title cannot contain only numbers.")

        else:
            return title


# ============================================================
# DESCRIPTION VALIDATION
# ============================================================

# Function to get and validate task description
def get_description():

    while True:

        # Take description from the user
        description = input("Enter Task Description: ").strip()

        # Description cannot be empty
        if description == "":
            print("Description cannot be empty.")

        else:
            return description


# ============================================================
# PRIORITY VALIDATION
# ============================================================

# Function to get and validate task priority
def get_priority():

    while True:

        # Take priority from the user
        priority = input(
            "Enter Priority (High/Medium/Low): "
        ).strip().lower()

        # Accept only valid priorities
        if priority == "high":
            return "High"

        elif priority == "medium":
            return "Medium"

        elif priority == "low":
            return "Low"

        else:
            print("Invalid priority! Choose High, Medium or Low.")


# ============================================================
# DATE VALIDATION
# ============================================================

# Function to get and validate task due date
def get_due_date():

    while True:

        # Take due date from the user
        due_date = input(
            "Enter Due Date (DD-MM-YYYY): "
        ).strip()

        try:

            # Convert entered string into a date object
            date_object = datetime.strptime(
                due_date,
                "%d-%m-%Y"
            )

            # Check whether the date is in the past
            if date_object.date() < datetime.now().date():

                print("Due date cannot be in the past.")
                continue

            # Return valid date
            return due_date

        except ValueError:

            # Handle invalid date
            print(
                "Invalid date! Please enter a valid date "
                "in DD-MM-YYYY format."
            )


# ============================================================
# ADD TASK
# ============================================================

# Function to add a new task
def add_task():

    print("\n--- Add New Task ---")

    # Get validated task details
    task_id = get_task_id()
    title = get_title()
    description = get_description()
    priority = get_priority()
    due_date = get_due_date()

    # Create a Task object
    task = Task(
        task_id,
        title,
        description,
        priority,
        due_date
    )

    # Add the task object to the task list
    tasks.append(task)

    print("\nTask added successfully!")


# ============================================================
# MAIN PROGRAM
# ============================================================

# Run the main menu continuously
while True:

    print("\n===== Smart Task Management System =====")
    print("1. Add Task")
    print("2. Exit")

    # Take menu choice from the user
    choice = input("Enter your choice: ").strip()

    # Add a new task
    if choice == "1":
        add_task()

    # Exit the program
    elif choice == "2":
        print("\nThank you for using Smart Task Management System!")
        break

    # Handle invalid menu choice
    else:
        print("Invalid choice! Please enter 1 or 2.")