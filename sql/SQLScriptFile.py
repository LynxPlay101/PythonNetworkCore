import sqlite3
from sqlite3 import Cursor

import mysql
from mysql import connector


class SQLScriptFile:
    file: str

    def __init__(self, file: str):
        self.file = file
        pass

    def execute(self, c: Cursor):
        file_reader = open(self.file, 'r')
        script = file_reader.read()
        file_reader.close()

        calls = script.split(";")
        for call in calls:
            try:
                c.execute(call)
            except sqlite3.DatabaseError as error:
                print(error)
                print("On call %s" % call)
            except mysql.connector.errors.DatabaseError as error:
                print(error)
                print("On call %s" % call)
        pass
