from typing import Tuple, List
from uuid import UUID

from player.profiles.NetworkPlayer import NetworkPlayer
from player.profiles.PlayerProfile import PlayerProfile
from player.profiles.PlayerProfileSnapshot import PlayerProfileSnapshot
from player.profiles.SelectedProfileData import SelectedProfileData
from player.dao.PlayerProfileDao import PlayerProfileDao
from player.dao.PlayerProfileSnapshotDao import PlayerProfileSnapshotDao
from player.dao.SelectedProfileDataDao import SelectedProfileDataDao
from sql.GenericDao import GenericDao
from sql.SQLProvider import SQLProvider


def get_selected_snapshot(selected_profile_data: SelectedProfileData, snapshots: List[PlayerProfileSnapshot],
                          branch: str) -> PlayerProfileSnapshot:
    profile_id = selected_profile_data.get_profile(branch)
    if profile_id is None:
        raise BaseException("Here we would have to create a new snapshot woop, woop")

    for x in snapshots:
        if x.profile_id == profile_id:
            return x
    raise BaseException("Could not find selected profile in player profile list")
    pass


class NetworkPlayerDao(GenericDao[NetworkPlayer]):
    server_branch: str
    selected_profile_dao: SelectedProfileDataDao
    profile_dao: PlayerProfileDao
    snapshot_dao: PlayerProfileSnapshotDao

    def __init__(self, sql_provider: SQLProvider
                 , selected_profile_dao: SelectedProfileDataDao
                 , snapshot_dao: PlayerProfileSnapshotDao
                 , profile_dao: PlayerProfileDao
                 , server_branch: str):
        super().__init__(sql_provider, "network_players", [["uuid", "_binary %s"]]
                         , lambda t: self.load_network_player(t))
        self.server_branch = server_branch
        self.snapshot_dao = snapshot_dao
        self.profile_dao = profile_dao
        self.selected_profile_dao = selected_profile_dao

    def load_network_player(self, t: Tuple) -> NetworkPlayer:
        player_uuid = UUID(bytes=bytes(t[0]))

        selected_profile_data: SelectedProfileData = self.selected_profile_dao.lookup([("uuid", player_uuid.bytes)])
        snapshots: List[PlayerProfileSnapshot] = self.snapshot_dao.lookup_all(player_uuid)
        player_profile: PlayerProfile = self.profile_dao.from_snapshot(
            get_selected_snapshot(selected_profile_data, snapshots, self.server_branch))

        return NetworkPlayer(t[1], t[2], t[3], t[4], selected_profile_data, player_profile, snapshots)

    pass
