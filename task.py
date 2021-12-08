import typer

app = typer.Typer()


@app.command()
def help():
    """Show usage"""
    print("""Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
""")


@app.command()
def add(priority: int, text: str):
    """Add a new item with priority <priority> and text <text> to the list"""

    # find less than or equal to priority index
    priority_index = 0
    tasks = []

    try:
        with open("task.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_priority, task_text = task.split(" ", 1)
                if int(task_priority) <= priority:
                    priority_index += 1

            if int(priority_index) <= priority:
                with open("task.txt", "a") as file:
                    print(f"{priority} {text}")
                    file.write(f"{priority} {text}\n")
            else:
                tasks_count = len(tasks)
                with open("task.txt", "w") as file:
                    for i in range(tasks_count):
                        if i != priority_index:
                            file.write(tasks[i])
                        else:
                            file.write(f"{priority} {text}\n")
                            file.write(tasks[i])

    except FileNotFoundError:
        with open("task.txt", "a") as file:
            print(f"{priority} {text}")
            file.write(f"{priority} {text}\n")

    print(f'Added task: "{text}" with priority {priority}')

    print(priority_index)


@app.command()
def Del(index: int):
    """Delete the incomplete item with the given index"""

    delete_task = ""
    try:
        with open("task.txt", "r") as file:
            tasks = file.readlines()
            delete_task = tasks[index - 1]

        with open("task.txt", "w") as file:
            for task in tasks:
                if task != delete_task:
                    file.write(task)

        print(f"Deleted task #{index}")

    except IndexError:
        print(
            f"Error: item with index {index} does not exist. Nothing deleted.")


@app.command()
def ls():
    """Show incomplete priority list items sorted by priority in ascending order"""
    with open("task.txt", "r") as file:
        lines = file.readlines()
        lines_count = len(lines)
        for i in range(lines_count):
            task = lines[i].split(" ", 1)
            print(f"{i+1}. {task[1][:-1]} [{task[0]}]")


@app.command()
def report():
    """Statistics"""

    try:
        with open("task.txt", "r") as file:
            lines = file.readlines()
            lines_count = len(lines)
            print(f"Pending : {lines_count}")
            for i in range(lines_count):
                task = lines[i].split(" ", 1)
                print(f"{i+1}. {task[1][:-1]} [{task[0]}]")
    except FileNotFoundError:
        print(f"Pending : {0}")

    try:
        with open("completed.txt", "r") as file:
            lines = file.readlines()
            lines_count = len(lines)
            print(f"\nCompleted : {len(lines)}")
            for i in range(lines_count):
                print(f"{i+1}. {lines[i]}", end="")
    except FileNotFoundError:
        print(f"\nCompleted : {0}")


@app.command()
def done(index: int):
    """Mark the incomplete item with the given index as complete"""

    done_task = ""
    try:
        with open("task.txt", "r") as file:
            tasks = file.readlines()
            done_task = tasks[index - 1]

        with open("task.txt", "w") as file:
            for task in tasks:
                if task != done_task:
                    file.write(task)

        with open("completed.txt", "a") as file:
            file.write(done_task.split(" ", 1)[1])

        print("Marked item as done.")

    except IndexError:
        print(f"Error: no incomplete item with index {index} exists.")


if __name__ == '__main__':
    print("""Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
""")
    app()
