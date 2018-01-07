import sqlite3


def makeConnection():
    global conn
    conn = sqlite3.connect('computers.db')
    global cursor
    cursor = conn.cursor()
    print("Connected to sqlite db")

def closeConnection():
    conn.commit()
    conn.close()
    print("Connection closed")

def createTable():
    print (cursor)
    if cursor == None:
        print("Connection failure, make sure you are connected to db")
    else:
        cursor.execute("""
            DROP TABLE if exists computers
            """)
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
                bandwidth  INTEGER NOT NULL
            , UNIQUE (pricehr, pricemo, cpus, memram, memssd, bandwidth) ON CONFLICT REPLACE);
        """)
        print('Table was successfully created.')

def tableInsert(data):
    if cursor == None:
        print("Connection failure, make sure you are connected to db")
    else:
        cursor.execute("""
        INSERT INTO computers (name, service, pricehr, pricemo, cpus, memram, memssd, bandwidth)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))

def tableSave():
    if conn == None:
        print ("Error, sqlite is not connected")
    else:
        conn.commit()
