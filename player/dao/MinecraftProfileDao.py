from typing import Tuple

from player.profiles.MinecraftProfile import MinecraftProfile
from sql.GenericDao import GenericDao
from sql.SQLProvider import SQLProvider


class MinecraftProfileDao(GenericDao[MinecraftProfile]):

    def __init__(self, sql_provider: SQLProvider):
        super().__init__(sql_provider, "minecraft_profile", [["profile_id", "%s"]]
                         , lambda t: self.load_profile(t))

    def load_profile(self, t: Tuple) -> MinecraftProfile:
        return MinecraftProfile(t[0], t[1], t[2])

    pass
