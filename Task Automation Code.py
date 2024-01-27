class Task:
    def __init__(self, date, task_name, priority, status):
        self.date = date
        self.task_name = task_name
        self.priority = priority
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def display_tasks(self):
        for task in self.tasks:
            print(f"Date: {task.date}, Task: {task.task_name}, Priority: {task.priority}, Status: {task.status}")

    def add_task_interactively(self):
        date = input("Enter task date (YYYY-MM-DD): ")
        task_name = input("Enter task name: ")
        priority = input("Enter task priority: ")
        status = input("Enter task status (Not Started/In Progress/Done): ")

        new_task = Task(date, task_name, priority, status)
        self.add_task(new_task)
        print("Task added successfully!")

    def update_task_status(self):
        task_name = input("Enter the name of the task to update status: ")
        for task in self.tasks:
            if task.task_name == task_name:
                new_status = input("Enter the new status (Not Started/In Progress/Done): ")
                task.status = new_status
                print(f"Status of task '{task_name}' updated to '{new_status}'")
                return
        print(f"Task with name '{task_name}' not found.")

# Example Usage:
todo_list = ToDoList()

task1 = Task("2024-01-18", "Complete Assignment", "High", "Not Started")
task2 = Task("2024-01-19", "Prepare Presentation", "Medium", "In Progress")
task3 = Task("2024-01-20", "Submit Report", "Low", "Done")

todo_list.add_task(task1)
todo_list.add_task(task2)
todo_list.add_task(task3)

while True:
    print("\n===== To-Do List Menu =====")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Update Task Status")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        todo_list.display_tasks()
    elif choice == "2":
        todo_list.add_task_interactively()
    elif choice == "3":
        todo_list.update_task_status()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
