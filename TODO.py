import json
from datetime import datetime

FILENAME = "tasks.json"


def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    for number, task in enumerate(tasks, start=1):
        deadline = task.get("deadline", "no deadline")
        priority = task.get("priority", "medium")
        print(number, task["title"], "| due:", deadline, "| priority:", priority, "|", task["status"])


def ask_title(prompt):
    while True:
        text = input(prompt).strip()
        if text:
            return text
        print("The title cannot be empty.")


def ask_deadline():
    while True:
        text = input("Deadline (YYYY-MM-DD): ")
        try:
            datetime.strptime(text, "%Y-%m-%d")
            return text
        except ValueError:
            print("Please use the format YYYY-MM-DD, for example 2026-12-20.")


def ask_priority():
    while True:
        text = input("Priority (low/medium/high): ").lower()
        if text in ["low", "medium", "high"]:
            return text
        print("Please type low, medium, or high.")


def ask_task_number(tasks, action):
    try:
        number = int(input("Which task number to " + action + "? "))
    except ValueError:
        print("Please type a number.")
        return None
    if number < 1 or number > len(tasks):
        print("That task number does not exist.")
        return None
    return number - 1


def filter_tasks(tasks):
    print("\nFilter by:")
    print("1. Pending tasks")
    print("2. Done tasks")
    print("3. Low priority")
    print("4. Medium priority")
    print("5. High priority")
    option = input("Choose a filter: ")

    if option == "1":
        result = [t for t in tasks if t["status"] == "pending"]
    elif option == "2":
        result = [t for t in tasks if t["status"] == "done"]
    elif option == "3":
        result = [t for t in tasks if t.get("priority", "medium") == "low"]
    elif option == "4":
        result = [t for t in tasks if t.get("priority", "medium") == "medium"]
    elif option == "5":
        result = [t for t in tasks if t.get("priority", "medium") == "high"]
    else:
        print("Invalid filter.")
        return

    if not result:
        print("No tasks match this filter.")
    else:
        show_tasks(result)


tasks = load_tasks()

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Edit task")
    print("6. Filter tasks")
    print("7. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        title = ask_title("Task: ")
        deadline = ask_deadline()
        priority = ask_priority()
        task = {"title": title, "deadline": deadline, "priority": priority, "status": "pending"}
        tasks.append(task)
        save_tasks(tasks)
        print("Task added!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            show_tasks(tasks)

    elif choice == "3":
        if not tasks:
            print("No tasks yet.")
        else:
            show_tasks(tasks)
            index = ask_task_number(tasks, "mark as done")
            if index is not None:
                tasks[index]["status"] = "done"
                save_tasks(tasks)
                print("Task marked as done!")

    elif choice == "4":
        if not tasks:
            print("No tasks yet.")
        else:
            show_tasks(tasks)
            index = ask_task_number(tasks, "delete")
            if index is not None:
                removed = tasks.pop(index)
                save_tasks(tasks)
                print("Deleted:", removed["title"])

    elif choice == "5":
        if not tasks:
            print("No tasks yet.")
        else:
            show_tasks(tasks)
            index = ask_task_number(tasks, "edit")
            if index is not None:
                tasks[index]["title"] = ask_title("New title: ")
                save_tasks(tasks)
                print("Task updated!")

    elif choice == "6":
        if not tasks:
            print("No tasks yet.")
        else:
            filter_tasks(tasks)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")