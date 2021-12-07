#!/usr/bin/python3

import click

@click.group()
def cli():
    pass

@cli.command(name="add")
def add():
    pass

@cli.command(name="help")
def help():
    click.echo("""Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics
""")
    
@cli.command(name="")
def ls(): 



if __name__ == '__main__':
    cli()
