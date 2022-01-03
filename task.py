import sys
import typer
from typing import Optional

app = typer.Typer()


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
def add(priority: Optional[int] = typer.Argument(-1), text: Optional[str] = typer.Argument(None)):
    """Add a new item with priority <priority> and text <text> to the list"""

    # If priority is not specified, print Error
    if priority == -1:
        typer.echo("Error: Missing tasks string. Nothing added!")
        exit()

    # If text is not specified, print Error
    if text is None:
        typer.echo("Error: Missing tasks string. Nothing added!")
        exit()

    priority_index = 0
    tasks = []  # Tasks List

    # If file is already present
    try:
        # find less than or equal to priority index to store tasks in sorted order
        with open("task.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_priority, task_text = task.split(" ", 1)
                if int(task_priority) <= priority:
                    priority_index += 1

        # if new task has highest(numeric) priority, add it to the end of the list
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
                        # New task at sorted correct position
                        file.write(f"{priority} {text}\n")
                        file.write(tasks[i])

    # If file not present, Create a new one
    except FileNotFoundError:
        with open("task.txt", "w") as file:
            file.write(f"{priority} {text}\n")

    typer.echo(f'Added task: "{text}" with priority {priority}')


@app.command()
def Del(index: Optional[int] = typer.Argument(-1)):
    """Delete the incomplete item with the given index"""

    # If index is not specified, print Error
    if index == -1:
        typer.echo("Error: Missing NUMBER for deleting tasks.")
        exit()

    # If index is 0, print Error with not exist message
    if index == 0:
        typer.echo(f"Error: task with index #0 does not exist. Nothing deleted.")
        exit()

    delete_task = ""    # Task to be deleted

    # If index is Valid
    try:
        # Get the task to be deleted
        with open("task.txt", "r") as file:
            tasks = file.readlines()
            delete_task = tasks[index - 1]

        # Write tasks in the file, except the task that to be deleted
        with open("task.txt", "w") as file:
            for task in tasks:
                if task != delete_task:
                    file.write(task)

        typer.echo(f"Deleted task #{index}")

    # If index is invalid
    except IndexError:
        typer.echo(
            f"Error: task with index #{index} does not exist. Nothing deleted.")


@app.command()
def ls():
    """Show incomplete priority list items sorted by priority in ascending order"""

    # If file is present
    try:
        # Print pending tasks, if present
        with open("task.txt", "r") as file:
            lines = file.readlines()
            lines_count = len(lines)
            if lines_count == 0:
                typer.echo("There are no pending tasks!")
            else:
                for i in range(lines_count):
                    task = lines[i].split(" ", 1)
                    typer.echo(f"{i+1}. {task[1][:-1]} [{task[0]}]")

    # If file is not present
    except FileNotFoundError:
        typer.echo("There are no pending tasks!")


@app.command()
def report():
    """Statistics"""

    # If file present, print pending tasks
    try:
        with open("task.txt", "r") as file:
            lines = file.readlines()
            lines_count = len(lines)
            typer.echo(f"Pending : {lines_count}")
            for i in range(lines_count):
                task = lines[i].split(" ", 1)
                typer.echo(f"{i+1}. {task[1][:-1]} [{task[0]}]")

    # If file not present, print pending task count 0
    except FileNotFoundError:
        typer.echo(f"Pending : {0}")

    # If file is present, print completed tasks
    try:
        with open("completed.txt", "r") as file:
            lines = file.readlines()
            lines_count = len(lines)
            typer.echo(f"\nCompleted : {len(lines)}")
            for i in range(lines_count):
                print(f"{i+1}. {lines[i]}", end="")

    # If file not present, print completed task count 0
    except FileNotFoundError:
        typer.echo(f"\nCompleted : {0}")


@app.command()
def done(index: Optional[int] = typer.Argument(-1)):
    """Mark the incomplete item with the given index as complete"""

    # If index is not specified, print Error
    if index == -1:
        typer.echo("Error: Missing NUMBER for marking tasks as done.")
        exit()

    # If index is 0, Print Error
    if index == 0:
        typer.echo("Error: no incomplete item with index #0 exists.")
        exit()

    done_task = ""  # Done task

    # If index is Valid
    try:
        # Get Done Task
        with open("task.txt", "r") as file:
            tasks = file.readlines()
            done_task = tasks[index - 1]

        # Write all task in task.txt file, except done task
        with open("task.txt", "w") as file:
            for task in tasks:
                if task != done_task:
                    file.write(task)

        # Write done task in completed.txt file
        with open("completed.txt", "a") as file:
            file.write(done_task.split(" ", 1)[1])

        typer.echo("Marked item as done.")

    # If index is Invalid
    except IndexError:
        typer.echo(f"Error: no incomplete item with index {index} exists.")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append("help")
    app()
