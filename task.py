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
    print(f'Added task: "{text}" with priority {priority}')


@app.command()
def ls():
    """Show incomplete priority list items sorted by priority in ascending order"""
    print("1. Pay Bills [3]")
    print("1. Pay Bills [3]")
    print("1. Pay Bills [3]")


@app.command()
def Del(index: int):
    """Delete the incomplete item with the given index"""
    print(f"Deleted task #{index}")


@app.command()
def report():
    """Statistics"""
    task_pending, task_completed = 0, 0
    print(f"Pending : {task_pending}")
    print("1. Pay Bills [3]")
    print("1. Pay Bills [3]")
    
    print(f"\nCompleted : {task_completed}")
    print("1. Pay Bills")

@app.command()
def done(task_priority: int):
    """Mark the incomplete item with the given index as complete"""
    print("Marked item as done.")


if __name__ == '__main__':
    app()
