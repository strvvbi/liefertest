import sqlite3


def insertVariableIntoTable(id, forname, lastname, address, zipCode, password):
  try: 
    connection = sqlite3.connect("lieferspatz.db")
    cursor = connection.cursor()
    print("Connected to SQLite")

    cursor.execute("create table client_accounts if not exists (id integer, forname text, lastname text, address text, zipCode text, password text)")
    print("Table exists")
    sqlite_insert_with_param = """insert into client_accounts (id, forname, lastname, address, zipCode, password) VALUES (?, ?, ?, ?, ?, ?), (id, forname, lastname, address, zipCode, password)"""

    cursor.execute(sqlite_insert_with_param)
    connection.commit()
    print("Python Variables inserted successfully into clients table")

    cursor.close()

  except sqlite3.Error as error: 
    print("Failed to insert Python variable into sqlite table", error)
  finally:
    if connection:
        connection.close()
        print("The SQLite connection is closed") 
  

insertVariableIntoTable(1, "Bettina", "Tugui", "Nettelbeckstr.10", "40477", "123456")   