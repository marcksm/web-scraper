import sqlite3
import pandas as pd

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

def dropTable():
    if cursor == None:
        print("Connection failure, make sure you are connected to db")
    else:
        cursor.execute("""
            DROP TABLE if exists computers
            """)
        print('Table was successfully dropped.')

def isTable():
    if cursor == None:
        print("Connection failure, make sure you are connected to db")
    else:
        cursor.execute("""
            select count(*) from sqlite_master where type='table' and name='computers';
            """)
        if (int(cursor.fetchall()[0][0])) == 1:
            return True
        else:
            return False

def createTable():
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
            , UNIQUE (pricehr, pricemo, cpus, memram, memssd, bandwidth) ON CONFLICT IGNORE);
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

def showTable():
    if conn == None or cursor == None:
        print ("Error, sqlite is not connected")
    else:
        cursor.execute("SELECT name, service, pricehr, pricemo, cpus, memram, memssd, bandwidth FROM computers;")
        pd.set_option('display.max_columns', 1000)
        pd.set_option('display.width', 1000)
        data = pd.DataFrame(cursor.fetchall())
        data.columns = ['Name', 'Site', '$ / hour', '$ / month', 'CPUs', 'RAM (GB)', 'Storage (GB)', 'Bandwidth (GB)']
        print(data)
