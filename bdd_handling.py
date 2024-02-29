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