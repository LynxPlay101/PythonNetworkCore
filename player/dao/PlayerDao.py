from typing import Tuple
from uuid import UUID

from player.profiles.Player import Player
from player.dao.NetworkPlayerDao import NetworkPlayerDao
from sql.GenericDao import GenericDao
from sql.SQLProvider import SQLProvider


class PlayerDao(GenericDao[Player]):
    network_player_dao: NetworkPlayerDao

    def __init__(self, provider: SQLProvider, network_player_dao: NetworkPlayerDao):
        super().__init__(provider, "players", [["uuid", "_binary %s"]]
                         , lambda t: self.load_player(t))
        self.network_player_dao = network_player_dao

    def load_player(self, t: Tuple) -> Player:
        player_uuid = UUID(bytes=bytes(t[0]))
        return Player(player_uuid, t[1], t[2], self.network_player_dao.lookup([player_uuid.bytes]))
