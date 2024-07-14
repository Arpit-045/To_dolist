# In-memory list to store tasks
tasks = []

# Function to display tasks
def display_tasks():
    if not tasks:
        print("No tasks to show.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{index}. {task['description']} [{status}]")

# Function to add a new task
def add_task():
    description = input("Enter the task description: ")
    tasks.append({"description": description, "completed": False})
    print("Task added.")

# Function to mark a task as complete
def complete_task():
    display_tasks()
    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as complete.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Function to delete a task
def delete_task():
    display_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        tasks.pop(task_number - 1)
        print("Task deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

# Main function to run the to-do list application
def main():
    while True:
        print("\nTo-Do List:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
