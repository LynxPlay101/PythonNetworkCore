import sqlite3
from multiprocessing.pool import Pool
from queue import Queue

from sqlite3 import Connection, Cursor
from typing import Callable

import mysql.connector


class SQLProvider:
    provider = None

    def __init__(self, provider):
        self.provider = provider

    def get(self) -> Connection:
        return self.provider.get()

    def offer(self, connection: Connection) -> None:
        self.provider.offer(connection)

    def prepare_connection(self) -> Connection:
        return self.provider.prepare_connection()

    def execute(self, consumer: Callable[[Cursor], None]) -> None:
        self.provider.execute(consumer)

    def close(self):
        self.provider.close()
        return


class SQLLiteProvider:
    connection: Connection
    file: str

    def __init__(self, file: str):
        self.file = file
        self.connection = None
        pass

    def get(self) -> Connection:
        if self.connection is None:
            self.connection = self.prepare_connection()
        return self.connection

    def offer(self, connection: Connection) -> None:
        connection.commit()
        connection.close()
        self.connection = None
        pass

    def prepare_connection(self) -> Connection:
        return sqlite3.connect(self.file)

    def execute(self, consumer: Callable[[Cursor], None]) -> None:
        connection = self.get()
        consumer(connection.cursor())
        self.offer(connection)

    def close(self):
        if self.connection is not None:
            self.connection.close()

    pass


class MySQLProvider:
    config: dict
    connection_pool: Queue

    def __init__(self, size: int, config: dict):
        self.config = config
        self.connection_pool = Queue()

        for x in range(size):
            self.offer(self.prepare_connection())

        pass

    def get(self) -> Connection:
        return self.connection_pool.get()

    def offer(self, connection: Connection) -> None:
        connection.commit()
        self.connection_pool.put_nowait(connection)

    def prepare_connection(self) -> Connection:
        return mysql.connector.connect(**self.config)

    def execute(self, consumer: Callable[[Cursor], None]) -> None:
        connection = self.get()
        consumer(connection.cursor())
        self.offer(connection)

    def close(self):
        while not self.connection_pool.empty():
            con: Connection = self.connection_pool.get()
            con.close()
        pass
    pass
