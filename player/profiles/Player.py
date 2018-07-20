from uuid import UUID

from player.profiles.NetworkPlayer import NetworkPlayer


class Player:
    uuid: UUID
    last_known_name: str
    last_known_ip: str

    network_player: NetworkPlayer

    def __init__(self, uuid: UUID, last_known_name: str, last_known_ip: str, network_player: NetworkPlayer):
        self.uuid = uuid
        self.last_known_name = last_known_name
        self.last_known_ip = last_known_ip
        self.network_player = network_player
        pass

    def __str__(self):
        return "Player{" + self.uuid.__str__() + " as " + self.last_known_name + " from " + self.last_known_ip \
               + "(" + (self.network_player is None and "" or str(self.network_player)) + ")" + "}"

