tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        title = input("Task: ")
        task = {"title": title, "status": "pending"}
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(number, task["title"], "-", task["status"])

    elif choice == "3":
        if not tasks:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(number, task["title"], "-", task["status"])
            number = int(input("Which task number is done? "))
            tasks[number - 1]["status"] = "done"
            print("Task marked as done!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")