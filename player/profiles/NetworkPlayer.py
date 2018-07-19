from sqlite3 import Timestamp, Date
from typing import List
from uuid import UUID

import util.ToStringUtil as sU
from player.profiles.PlayerProfile import PlayerProfile
from player.profiles.PlayerProfileSnapshot import PlayerProfileSnapshot
from player.profiles.SelectedProfileData import SelectedProfileData


class NetworkPlayer:
    first_login: Date
    last_login: Timestamp
    discord_id: str
    discourse_name: str

    selected_profile_data: SelectedProfileData
    current_profile: PlayerProfile
    profile_snapshots: List[PlayerProfileSnapshot]

    def __init__(self, first_login: Date, last_login: Timestamp, discord_id: str, discourse_name: str
                 , selected_profile_data: SelectedProfileData
                 , current_profile: PlayerProfile, profile_snapshots: List[PlayerProfileSnapshot]):
        self.first_login = first_login
        self.last_login = last_login
        self.discord_id = discord_id
        self.discourse_name = discourse_name
        self.current_profile = current_profile
        self.profile_snapshots = profile_snapshots
        self.selected_profile_data = selected_profile_data
        pass

    def __str__(self):
        return "NetworkPlayer{" + self.first_login.__str__() \
               + "," + self.last_login.__str__() \
               + "," + sU.or_else(self.discord_id, "N/A") \
               + "," + sU.or_else(self.discourse_name, "N/A") \
               + "(" + (self.current_profile is None and "N/A" or self.current_profile.__str__()) + ")" \
               + "(" + (self.profile_snapshots is None and "N/A" or sU.from_list(self.profile_snapshots)) + ")" \
               + "}"
