from task import add_task, list_tasks, complete_task, remove_task

WELCOME_MESSAGE = "Welcome to Task Manager CLI! Updated By Saditha"


def show_help():
    """Print available commands."""
    print("""
Commands:
  list              - Show all tasks
  add <task name>   - Add a new task
  done <id>         - Mark a task as done
  remove <id>       - Remove a task
  help              - Show this help message
  quit              - Exit the app
""")


def run():
    print("=" * 40)
    print(WELCOME_MESSAGE)
    print("=" * 40)
    show_help()

    while True:
        try:
            user_input = input("Enter command: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if not user_input:
            continue

        parts = user_input.split(maxsplit=1)
        command = parts[0].lower()

        if command == "quit":
            print("Goodbye!")
            break

        elif command == "list":
            list_tasks()

        elif command == "add":
            if len(parts) < 2 or not parts[1].strip():
                print("Usage: add <task name>")
            else:
                add_task(parts[1].strip())

        elif command == "done":
            if len(parts) < 2:
                print("Usage: done <task id>")
            else:
                try:
                    task_id = int(parts[1])
                    complete_task(task_id)
                except ValueError:
                    print("Please provide a valid task number. Example: done 1")

        elif command == "remove":
            if len(parts) < 2:
                print("Usage: remove <task id>")
            else:
                try:
                    task_id = int(parts[1])
                    remove_task(task_id)
                except ValueError:
                    print("Please provide a valid task number. Example: remove 1")

        elif command == "help":
            show_help()

        else:
            print(f"Unknown command: '{command}'. Type 'help' to see available commands.")


if __name__ == "__main__":
    run()