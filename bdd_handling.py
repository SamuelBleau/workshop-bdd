import sqlite3

"""
SQLite3 basic functions :
    db = sqlite3.connect('filename') : connect to the database of a file.
    cursor = db.cursor() : create a cursor to execute SQL commands.
    cursor.execute('SQL command') : execute a SQL command.
    db.commit() : commit the changes to the database.
    cursor.close() : close the cursor.
    db.close() : close the database.
"""

def create_table():
    return

def delete_table():
    return

def add_value(nom, type1, type2, description, poids, taille):
    return

def delete_value(id):
    return

def my_interactive_bdd():
    res = None
    while res != "exit":
        res = input("Entrez une commande : ")
        if res == "create table":
            create_table()
        elif res == "delete table":
            delete_table()
        elif res == "add":
            nom = input("Entrez le nom du pokémon : ")
            type1 = input("Entrez le type principal du pokémon : ")
            type2 = input("Entrez le type secondaire du pokémon : ")
            description = input("Entrez la description du pokémon : ")
            poids = input("Entrez le poids du pokémon : ")
            taille = input("Entrez la taille du pokémon : ")
            add_value(nom, type1, type2, description, poids, taille)
        elif res == "delete":
            id = input("Entrez l'id du pokémon à supprimer : ")
            delete_value(id)
    return

if __name__ == "__main__":
    my_interactive_bdd()