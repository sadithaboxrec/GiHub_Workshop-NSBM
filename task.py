from storage import load_tasks, save_tasks


def add_task(title):
    """Add a new task to the list."""
    tasks = load_tasks()
    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: '{title}'")
    print("Task created By Saditha")


def list_tasks():
    """Display all tasks with their status."""
    tasks = load_tasks()

    if not tasks:
        print("No tasks yet! Add one with: add <task name>")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "Correct" if task["done"] else "⬜"
        print(f"  [{task['id']}] {status}  {task['title']}")
    print()


def complete_task(task_id):
    """Mark a task as done by its ID."""
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as done!")
            return

    print(f"Task {task_id} not found.")


def remove_task(task_id):
    """Remove a task from the list by its ID."""
    tasks = load_tasks()
    original_count = len(tasks)

    tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == original_count:
        print(f"Task {task_id} not found.")
        return

    save_tasks(tasks)
    print(f"Task {task_id} removed.")