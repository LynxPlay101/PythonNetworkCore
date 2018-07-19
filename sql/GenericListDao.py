from typing import Generic, TypeVar, List, Tuple, Optional, Callable, MutableMapping

from sql.SQLProvider import SQLProvider

T = TypeVar("T")


def map_keys(key: List[List[str]]) -> MutableMapping[str, str]:
    result = {}
    for e in key:
        result[e[0]] = e[1]
    return result
    pass


class GenericListDao(Generic[T]):
    table: str
    key_map: MutableMapping[str, str]
    provider: SQLProvider
    mapper: Callable[[Tuple], T]

    def __init__(self, provider: SQLProvider, table: str, key: List[List[str]]
                 , mapper: Callable[[List[Tuple]], T]):
        self.provider = provider
        self.key_map = map_keys(key)
        self.table = table
        self.mapper = mapper
        pass

    def lookup(self, key: List[Tuple[str, object]]) -> Optional[T]:
        connection = self.provider.get()
        c = connection.cursor()

        query, keys = self.prepare_keys(key)

        c.execute(query, keys)
        result_set = c.fetchall()

        self.provider.offer(connection)
        c.close()

        if result_set is None:
            return None
        if len(result_set) < 1:
            return []

        mapped_result: T = self.mapper(result_set)
        return mapped_result

    def prepare_keys(self, key: List[Tuple[str, object]]) -> Tuple[str, List[object]]:
        query = "SELECT * FROM " + self.table + " WHERE "

        keys: List[object] = []
        for index in range(len(key)):
            name = key[index][0]
            col_type = self.key_map[key[index][0]]

            query += (index > 0 and " AND " or "")
            query += name + " = " + col_type
            keys.append(key[index][1])

        return query, keys
