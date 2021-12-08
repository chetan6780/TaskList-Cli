import typer
import sys

app = typer.Typer()

# prints help when no additional args are provided


@app.command()
@app.command()
def help():
    """Show usage"""
    typer.echo("""Usage :-
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

    priority_index = 0
    tasks = []

    try:
        # find less than or equal to priority index
        with open("task.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_priority, task_text = task.split(" ", 1)
                if int(task_priority) <= priority:
                    priority_index += 1

        # if new task has highest priority, add it to the end of the list
        if int(priority_index) == len(tasks):
            with open("task.txt", "a") as file:
                file.write(f"{priority} {text}\n")
        # Else add it after the less than or equal priority task
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
            file.write(f"{priority} {text}\n")

    typer.echo(f'Added task: "{text}" with priority {priority}')


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
    if len(sys.argv) <= 1:
        sys.argv.append("help")
    app()
