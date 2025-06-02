def show_menu():
    print("\nTo-Do List App")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task['done'] else "❌"
                print(f"{i}. {task['task']} [{status}]")

        elif choice == '2':
            new_task = input("Enter new task: ")
            tasks.append({"task": new_task, "done": False})
            print("Task added.")

        elif choice == '3':
            task_num = int(input("Enter task number to mark done: "))
            if 0 < task_num <= len(tasks):
                tasks[task_num - 1]['done'] = True
                print("Task marked as done.")

        elif choice == '4':
            task_num = int(input("Enter task number to delete: "))
            if 0 < task_num <= len(tasks):
                tasks.pop(task_num - 1)
                print("Task deleted.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
