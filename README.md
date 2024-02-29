# WORKSHOP-BDD

## Introduction:

SQLite is a version of MySQL wich doesn't require any server to work. It can only open and read one SQLite file at once.

### Prerequisites:

`Python` : installation : `sudo apt install python3`

`SQLite 3` : dans votre code python : `import sqlite3`

## Part one:

For this part you'll create basic SQLite functions in order to create/delete a table and interact with it.
Please disable copilot if you use it, the goal is to learn and understand how SQL works.

### Reminder:

First of all you must know how to use the sqlite3 library to make SQL with our python code.
These are the differents functions you'll need:

* db = sqlite3.connect('filename') : connect to the database of a file.
* cursor = db.cursor() : create a cursor to execute SQL commands.
* cursor.execute('SQL command') : execute a SQL command.
* db.commit() : commit the changes to the database.
* cursor.close() : close the cursor.
* db.close() : close the database.

### Step one:

Now you can start to write some SQL in your code. We will do the create_table() function in order to create a table named `pokedex`:

```python
def create_table():
```

This table must contain differents datas:
* int primary key id
* a `string` name
* a `string` type1
* a `string` type2
* a `string` description
* an `int` weight.
* an `int` height.

Help: You'll probably need `CREATE TABLE IF NOT EXISTS` to create a new table.

### Step two:

If you can create a table in your SQLite file, you must be able to delete it:

```python
def delete_table():
```

Help: `DROP TABLE` can be useful for this.

### Step three:

We will add some elements in our new data base.

```python
def add_value(nom, type1, type2, description, poids, taille):
```

Help: Use `INSERT INTO ... VALUES` function for this step.

### Step four :

Alike the delete_table() function, now you must know how to delete an element of the table with `DELETE FROM ... WHERE`.

```python
def delete_value(id):
```

### Final step:

Now, we will add everything we created together so as to make a completely functionnal data base. Copy the code below (or the `bdd_handling.py` file if you prefer):

```python
import sqlite3

def create_table():
    return

def delete_table():
    return

def add_value(name, type1, type2, description, weight, height):
    return

def delete_value(id):
    return

def my_interactive_bdd():
    res = None
    while res != "exit":
        res = input("Enter a command : ")
        if res == "create table":
            create_table()
        elif res == "delete table":
            delete_table()
        elif res == "add":
            name = input("Enter the name of the pokemon : ")
            type1 = input("Enter the first type of the pokemon : ")
            type2 = input("Enter the second type of the pokemon : ")
            description = input("Enter the description of the pokemon : ")
            weight = input("Enter the weight of the pokemon : ")
            height = input("Enter the height of the pokemon : ")
            add_value(name, type1, type2, description, weight, height)
        elif res == "delete":
            id = input("Enter the id of the pokemon : ")
            delete_value(id)
    return

if __name__ == "__main__":
    my_interactive_bdd()
```
