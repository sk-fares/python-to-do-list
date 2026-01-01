tasks = []

def addTask():
    task = input("Enter your task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")



def listTask():
    if len(tasks) == 0:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        i = 0
        while i < len(tasks):
            print("Task #", i + 1, ".", tasks[i])
            i = i + 1



def deleteTask():
    if len(tasks) == 0:
        print("There are no tasks to delete.")
        return

    listTask()

    try:
        taskToDelete = int(input("Enter the task number to delete: "))
        taskToDelete = taskToDelete - 1

        if taskToDelete >= 0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print("Task deleted successfully.")
        else:
            print("Task number not found.")

    except:
        print("Invalid Input.")




if __name__ == "__main__":
    # I created a loop to run the to-do app
    print("Welcome to the To-Do List App :)")

    while True:
        print("\nPlease select one of the following options")
        print("--------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List all tasks")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid Input. Please enter a number.")
            continue

        if choice == 1:
            addTask()
        elif choice == 2:
            deleteTask()
        elif choice == 3:
            listTask()
        elif choice == 4:
            print("Goodbye 👋👋")
            break
        else:
            print("Invalid option. Please try again.")
