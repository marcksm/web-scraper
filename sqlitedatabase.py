import sqlite3
conn = None
cursor = None

def makeConnection():
    conn = sqlite3.connect('computers.db')
    cursor = conn.cursor()
    print("Connected to sqlite db")

def closeConnection():
    conn.commit()
    conn.close()
    print("Connection closed")

def createTable():
    if cursor == None:
        print("Connection failure, make sure you are connected to db")
    else:
        cursor.execute("""
            CREATE TABLE computers (
                id         INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name       TEXT NOT NULL,
                service    TEXT NOT NULL,
                pricehr    REAL NOT NULL,
                pricemo    INTEGER NOT NULL,
                cpus       INTEGER NOT NULL,
                memram     INTEGER NOT NULL,
                memssd     INTEGER NOT NULL,
                bandwidth  INTEGER NOT NULL,
                created_at DATE NOT NULL
            );
        """)
        print('Table was successfully created.')

def tableInsert(data):
    if cursor == None:
        print("Connection failure, make sure you are connected to db")
    else:
        cursor.execute("""
        INSERT INTO computers (name, service, pricehr, pricemo, cpus, memram, memssd, bandwidth, created_at)
        VALUES (?)
        """, data)

def tableSave ():
    if conn == None:
        print ("Error, sqlite is not connected")
    else:
        conn.commit()
