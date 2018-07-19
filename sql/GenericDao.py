from typing import Generic, TypeVar, List, Tuple, Optional, Callable
import util.ToStringUtil as tSU

from mysql.connector import ProgrammingError

from sql.SQLProvider import SQLProvider

T = TypeVar("T")


class GenericDao(Generic[T]):
    table: str
    key: List[List[str]]
    select_query: str
    provider: SQLProvider
    mapper: Callable[[Tuple], T]

    def __init__(self, provider: SQLProvider, table: str, key: List[List[str]]
                 , mapper: Callable[[Tuple], T]):
        self.provider = provider
        self.key = key
        self.table = table
        self.mapper = mapper

        self.select_query = self.build_select_query()
        pass

    def lookup(self, key: List) -> Optional[T]:
        connection = self.provider.get()
        c = connection.cursor()

        try:
            c.execute(self.select_query, key)
        except ProgrammingError as error:
            print(self.select_query + " could not be executed with " + tSU.from_list(key))
            raise error

        result_set = c.fetchone()

        self.provider.offer(connection)
        c.close()

        if result_set is None:
            return None

        mapped_result: T = self.mapper(result_set)
        return mapped_result

    def build_select_query(self) -> str:
        query = "SELECT * FROM " + self.table + " WHERE "
        for index in range(len(self.key)):
            query += (index > 0 and " AND " or "")
            query += self.key[index][0] + " = " + self.key[index][1]
        return query
