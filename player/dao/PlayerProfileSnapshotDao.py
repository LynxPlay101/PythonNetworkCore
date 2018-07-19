from typing import Tuple, List
from uuid import UUID

from player.profiles.PlayerProfile import PlayerProfile
from player.profiles.PlayerProfileSnapshot import PlayerProfileSnapshot
from sql.GenericDao import GenericDao
from sql.SQLProvider import SQLProvider


class PlayerProfileSnapshotDao(GenericDao[PlayerProfile]):

    def __init__(self, sql_provider: SQLProvider):
        super().__init__(sql_provider, "profiles", [["profile_id", "%s"]]
                         , lambda t: load_profile_snapshot(t))

    def lookup_all(self, uuid: UUID) -> List[PlayerProfileSnapshot]:
        connection = self.provider.get()
        c = connection.cursor()

        c.execute('SELECT * FROM profiles WHERE uuid = _binary %s', [uuid.bytes])

        result = []
        for row in c.fetchall():
            result.append(load_profile_snapshot(row))

        c.close()
        self.provider.offer(connection)
        return result

    pass


def load_profile_snapshot(t: Tuple) -> PlayerProfileSnapshot:
    return PlayerProfileSnapshot(t[0], t[2], t[3], t[4], t[5])
