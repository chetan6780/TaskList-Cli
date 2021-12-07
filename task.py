import typer    

app = typer.Typer()

@app.command()
def help():
    print("""Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
""")
    
@app.command()
def add(priority: int, task: str):
    """Add a new item with priority <priority> and text <text> to the list"""
    print(f"Added item with priority {priority} and text {task}")

    
@app.command()
def done(itemNum:int):
    print("Marked item as done.")
    
if __name__ == '__main__':
    app()
    