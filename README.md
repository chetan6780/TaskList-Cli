# TaskList - CLI

Here is the [Demo of CLI Application](https://www.youtube.com/watch?v=SjMk3ipwY9Y).

<!-- <iframe width="560" height="315" src="https://www.youtube.com/embed/SjMk3ipwY9Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe> -->

<!-- [![TASK-CLI](https://res.cloudinary.com/sv-co/image/upload/v1638058186/GDC/SE/Admission/gdc-home-page_b6s3go.png)](https://vimeo.com/648902045) -->

## Getting started

-   Check if python is installed,
    ```sh
    python3 --version
    ```
-   If Python is installed, you should be able to run cli application by following command:

    -   **On Windows:**

        ```sh
        .\task.bat
        ```

    -   **On \*nix:**
        ```sh
        ./task.sh
        ```

-   Else install python and run above command again.

## Install dependencies

```sh
>> npm install
>> pip install -r requirements.txt
```

## Create Create symbolic link to the executable file

#### On Windows

Run Windows Command Prompt or Windows Powershell **with administrator privileges**.

**Command Prompt:**

```sh
>> mklink task task.bat
```

**Powershell:**

```sh
>> cmd /c mklink task task.bat
```

#### On \*nix:

Run the following command in your shell:

```sh
>> ln -s task.sh task
```

## Usage

### 1. Help

Executing the command **without any arguments** or with a single argument **_help_** prints the **CLI usage**.

```sh
>> ./task help
Usage :-
./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
./task ls                   # Show incomplete priority list items sorted by priority in ascending order
./task del INDEX            # Delete the incomplete item with the given index
./task done INDEX           # Mark the incomplete item with the given index as complete
./task help                 # Show usage
./task report               # Statistics
```

### 2. List all pending items

Use the **_ls_** command to see all the items that are not yet complete, in **ascending order of priority**.

```sh
[index] [task] [priority]
```

Example:

```sh
>> ./task ls
1. change light bulb [2]
2. water the plants [5]
```

### 3. Add a new item

Use the **_add_** command. The text of the task should be enclosed within **double quotes**.

```sh
>> ./task add 5 "the thing i need to do"
Added task: "the thing i need to do" with priority 5
```

### 4. Delete an item

Use the **_del_** command to remove an item **by its index**.

```sh
>> ./task del 3
Deleted item with index 3
```

### 5. Mark a task as completed

Use the **_done_** command to mark an item as completed **by its index**.

```sh
>> ./task done 1
Marked item as done.
```

### 6. Generate a report

Use **\*report** command to view the number of **complete and incomplete items** in the list.

```sh
>> ./task report
Pending : 2
1. this is a pending task [1]
2. this is a pending task with priority [4]

Completed : 3
1. completed task
2. another completed task
3. yet another completed task
```
