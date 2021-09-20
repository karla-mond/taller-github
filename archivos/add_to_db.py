import sqlite3
from sqlite3.dbapi2 import Cursor

def main():
    con = sqlite3.connect('datos.db')
    cur = con.cursor()

    cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='datos' ''')

    if cur.fetchone()[0] == 0:
        # Table doesnt exist
        cur.execute('''CREATE TABLE datos
               (nombre text, animal text, lang text)''')

    insert_data(cur)

    con.commit()
    print("Datos guardados exitosamente") # Flagger

    con.close()

def insert_data(database: Cursor):
    prompts = ["Nombre: ", "Animal Favorito: ", "Lenguaje de progra fav: "]
    res = []

    for i in prompts:
        print(i)
        x = input()
        res.append(x)

    name, animal, lang = res

    database.execute(f"INSERT INTO datos VALUES ({name}, {animal}, {lang})")

if __name__ == "__main__":
    main()