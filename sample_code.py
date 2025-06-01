class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("Your To-Do List:")
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i + 1}. [{status}] {task['task']}")

    def complete_task(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")


def main():
    todo_list = TodoList()

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            try:
                task_num = int(input("Enter the task number to complete: "))
                todo_list.complete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Exiting To-Do List app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main() 