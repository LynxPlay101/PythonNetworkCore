from uuid import UUID

from player.profiles.MinecraftProfile import MinecraftProfile
from player.profiles.PlayerProfileSnapshot import PlayerProfileSnapshot
from player.profiles.roleplay.BranchProfile import BranchProfile


class PlayerProfile(PlayerProfileSnapshot):
    minecraft_profile: MinecraftProfile
    branch_profile: BranchProfile

    def __init__(self, profile_id: int, branch: str, first_name: str, last_name: str, gender: str
                 , minecraft_profile: MinecraftProfile
                 , branch_profile: BranchProfile):
        super().__init__(profile_id, branch, first_name, last_name, gender)
        self.minecraft_profile = minecraft_profile
        self.branch_profile = branch_profile
        pass

    pass
