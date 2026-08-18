from datetime import datetime


# ============================================================
# TASK CLASS
# ============================================================

# Class to represent a single task
class Task:

    # Initialize task details
    def __init__(self, task_id, title, description, priority, due_date):

        self.task_id = task_id          # Unique ID of the task
        self.title = title              # Title of the task
        self.description = description  # Description of the task
        self.priority = priority        # Priority of the task
        self.due_date = due_date        # Deadline of the task
        self.status = "Pending"         # Default status of the task


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

    # Keep asking until a valid ID is entered
    while True:

        try:
            # Take Task ID from the user
            task_id = int(input("Enter Task ID: "))

            # Task ID must be greater than zero
            if task_id <= 0:
                print("Task ID must be greater than 0.")
                continue

            # Check whether the Task ID already exists
            for task in tasks:

                if task.task_id == task_id:

                    # Display error for duplicate ID
                    print("Task ID already exists! Enter a different ID.")
                    break

            else:
                # Return the ID if it is unique
                return task_id

        except ValueError:

            # Handle non-numeric input
            print("Invalid input! Task ID must be a number.")


# ============================================================
# TITLE VALIDATION
# ============================================================

# Function to get and validate task title
def get_title():

    # Keep asking until a valid title is entered
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
            # Return valid title
            return title


# ============================================================
# DESCRIPTION VALIDATION
# ============================================================

# Function to get and validate task description
def get_description():

    # Keep asking until a valid description is entered
    while True:

        # Take description from the user
        description = input("Enter Task Description: ").strip()

        # Description cannot be empty
        if description == "":
            print("Description cannot be empty.")

        else:
            # Return valid description
            return description


# ============================================================
# PRIORITY VALIDATION
# ============================================================

# Function to get and validate task priority
def get_priority():

    # Keep asking until a valid priority is entered
    while True:

        # Take priority from the user
        priority = input(
            "Enter Priority (High/Medium/Low): "
        ).strip().lower()

        # Check for High priority
        if priority == "high":
            return "High"

        # Check for Medium priority
        elif priority == "medium":
            return "Medium"

        # Check for Low priority
        elif priority == "low":
            return "Low"

        else:
            # Display error for invalid priority
            print(
                "Invalid priority! "
                "Choose High, Medium or Low."
            )


# ============================================================
# DATE VALIDATION
# ============================================================

# Function to get and validate task due date
def get_due_date():

    # Keep asking until a valid date is entered
    while True:

        # Take due date from the user
        due_date = input(
            "Enter Due Date (DD-MM-YYYY): "
        ).strip()

        try:

            # Convert the entered string into a date object
            date_object = datetime.strptime(
                due_date,
                "%d-%m-%Y"
            )

            # Check whether the date is in the past
            if date_object.date() < datetime.now().date():

                # Display error for past date
                print("Due date cannot be in the past.")
                continue

            # Return valid due date
            return due_date

        except ValueError:

            # Handle invalid date format or invalid date
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

    # Get validated Task ID
    task_id = get_task_id()

    # Get validated task title
    title = get_title()

    # Get validated task description
    description = get_description()

    # Get validated task priority
    priority = get_priority()

    # Get validated due date
    due_date = get_due_date()

    # Create a new Task object
    task = Task(
        task_id,
        title,
        description,
        priority,
        due_date
    )

    # Add the task object to the task list
    tasks.append(task)

    # Display success message
    print("\nTask added successfully!")


# ============================================================
# VIEW TASKS
# ============================================================

# Function to display all tasks
def view_tasks():

    print("\n--- All Tasks ---")

    # Check whether the task list is empty
    if len(tasks) == 0:

        # Display message if no task is available
        print("No tasks available.")
        return

    # Loop through all task objects
    for task in tasks:

        # Display separator
        print("\n------------------------------")

        # Display Task ID
        print("Task ID     :", task.task_id)

        # Display Task Title
        print("Title       :", task.title)

        # Display Task Description
        print("Description :", task.description)

        # Display Task Priority
        print("Priority    :", task.priority)

        # Display Task Due Date
        print("Due Date    :", task.due_date)

        # Display Task Status
        print("Status      :", task.status)

        # Display closing separator
        print("------------------------------")

# ============================================================
# UPDATE TASK
# ============================================================

# Function to update an existing task
def update_task():

    print("\n--- Update Task ---")

    # Check whether any task exists
    if len(tasks) == 0:
        print("No tasks available to update.")
        return

    # Ask the user for the Task ID
    try:
        task_id = int(input("Enter Task ID to update: "))
    except ValueError:
        print("Invalid input! Task ID must be a number.")
        return

    # Search for the task with the given ID
    for task in tasks:

        if task.task_id == task_id:

            # Display update options
            print("\nWhat do you want to update?")
            print("1. Title")
            print("2. Description")
            print("3. Priority")
            print("4. Due Date")
            print("5. Cancel")

            choice = input("Enter your choice: ").strip()

            # Update task title
            if choice == "1":
                task.title = get_title()
                print("Task title updated successfully!")

            # Update task description
            elif choice == "2":
                task.description = get_description()
                print("Task description updated successfully!")

            # Update task priority
            elif choice == "3":
                task.priority = get_priority()
                print("Task priority updated successfully!")

            # Update task due date
            elif choice == "4":
                task.due_date = get_due_date()
                print("Task due date updated successfully!")

            # Cancel update
            elif choice == "5":
                print("Update cancelled.")

            else:
                print("Invalid choice! Please choose 1 to 5.")

            # Stop searching after finding the task
            return

    # Display message if Task ID was not found
    print("Task ID not found.")

# ============================================================
# DELETE TASK
# ============================================================

# Function to delete an existing task
def delete_task():

    print("\n--- Delete Task ---")

    # Check whether any task exists
    if len(tasks) == 0:
        print("No tasks available to delete.")
        return

    # Ask the user for the Task ID
    try:
        task_id = int(input("Enter Task ID to delete: "))

    except ValueError:
        # Handle non-numeric Task ID
        print("Invalid input! Task ID must be a number.")
        return

    # Search for the task with the given ID
    for task in tasks:

        if task.task_id == task_id:

            # Ask for confirmation before deleting
            print("\nTask found:")
            print("Title :", task.title)
            print("Priority :", task.priority)

            confirmation = input(
                "Are you sure you want to delete this task? (Yes/No): "
            ).strip().lower()

            # Delete the task if user confirms
            if confirmation == "yes":

                tasks.remove(task)

                print("Task deleted successfully!")

            # Cancel deletion
            elif confirmation == "no":

                print("Task deletion cancelled.")

            else:

                print("Invalid choice! Please enter Yes or No.")

            # Stop searching after finding the task
            return

    # Display message if Task ID was not found
    print("Task ID not found.")

# ============================================================
# COMPLETE TASK
# ============================================================

# Function to mark a task as completed
def complete_task():

    print("\n--- Complete Task ---")

    # Check whether any task exists
    if len(tasks) == 0:
        print("No tasks available.")
        return

    # Ask the user for the Task ID
    try:
        task_id = int(input("Enter Task ID to complete: "))

    except ValueError:
        # Handle non-numeric Task ID
        print("Invalid input! Task ID must be a number.")
        return

    # Search for the task with the given ID
    for task in tasks:

        if task.task_id == task_id:

            # Check if task is already completed
            if task.status == "Completed":
                print("Task is already completed.")
                return

            # Change task status
            task.status = "Completed"

            # Display success message
            print("Task marked as completed successfully!")

            return

    # Display message if Task ID was not found
    print("Task ID not found.")


# ============================================================
# MAIN PROGRAM
# ============================================================

# Run the main menu continuously
while True:

    # Display the main menu
    print("\n===== Smart Task Management System =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Complete Task")
    print("6. Exit")

    # Take menu choice from the user
    choice = input("Enter your choice: ").strip()

    # Check whether the user wants to add a task
    if choice == "1":

        # Call Add Task function
        add_task()

    # Check whether the user wants to view tasks
    elif choice == "2":

        # Call View Tasks function
        view_tasks()

    # Check whether the user wants to update a task
    elif choice == "3":
         
        # Update an existing task
         update_task()

    # Check whether the user wants to delete a task
    elif choice == "4":

        # Delete an existing task
        delete_task()
 
    elif choice == "5":

        # Mark a task as completed
        complete_task()

    # Check whether the user wants to exit
    elif choice == "6":

        # Display exit message
        print(
            "\nThank you for using "
            "Smart Task Management System!"
        )

        # Stop the program
        break

    else:

        # Handle invalid menu choice
        print(
            "Invalid choice! "
            "Please enter 1, 2, 3, 4 ,5 or 6."
        )