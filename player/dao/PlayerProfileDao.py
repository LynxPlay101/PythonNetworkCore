from typing import Tuple
from uuid import UUID

from player.profiles.PlayerProfile import PlayerProfile
from player.profiles.PlayerProfileSnapshot import PlayerProfileSnapshot
from player.dao.MinecraftProfileDao import MinecraftProfileDao
from player.dao.roleplay.BranchProfileDaoFactory import BranchProfileDaoFactory
from sql.GenericDao import GenericDao
from sql.SQLProvider import SQLProvider


class PlayerProfileDao(GenericDao[PlayerProfile]):
    minecraft_dao: MinecraftProfileDao
    branch_dao_factory: BranchProfileDaoFactory

    def __init__(self, sql_provider: SQLProvider,
                 branch_dao_factory: BranchProfileDaoFactory,
                 minecraft_dao: MinecraftProfileDao):
        super().__init__(sql_provider, "profiles", [["profile_id", "%s"]]
                         , lambda t: self.load_profile(t))
        self.minecraft_dao = minecraft_dao
        self.branch_dao_factory = branch_dao_factory

    def load_profile(self, t: Tuple) -> PlayerProfile:
        profile_id = t[0]
        branch = t[2]

        return PlayerProfile(profile_id, branch, t[3], t[4], t[5]
                             , self.minecraft_dao.lookup([profile_id]),
                             self.branch_dao_factory.get_dao(branch).lookup([profile_id]))

    def from_snapshot(self, snapshot: PlayerProfileSnapshot) -> PlayerProfile:
        return PlayerProfile(snapshot.profile_id, snapshot.branch, snapshot.first_name,
                             snapshot.last_name, snapshot.gender,
                             self.minecraft_dao.lookup([snapshot.profile_id]),
                             self.branch_dao_factory.get_dao(snapshot.branch).lookup([snapshot.profile_id]))

    pass
