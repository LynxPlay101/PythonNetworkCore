from uuid import UUID

import util.ToStringUtil as sU


class PlayerProfileSnapshot:
    profile_id: int
    branch: str
    first_name: str
    last_name: str
    gender: str

    def __init__(self, profile_id: int, branch: str, first_name: str, last_name: str, gender: str):
        self.profile_id = profile_id
        self.branch = branch
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        pass

    def __str__(self):
        return "ProfilePlayer{" + str(self.profile_id) \
               + "," + self.branch \
               + "," + sU.or_else(self.first_name, "N/A") \
               + "," + sU.or_else(self.last_name, "N/A") \
               + "," + sU.or_else(self.gender, "N/A") \
               + "}"
        pass
