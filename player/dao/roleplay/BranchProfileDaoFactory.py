from typing import MutableMapping

from player.dao.roleplay.BranchProfileDao import BranchProfileDao


class BranchProfileDaoFactory:
    dao_map: MutableMapping[str, BranchProfileDao]

    def __init__(self):
        self.dao_map = {}
        pass

    def register_dao(self, branch: str, dao: BranchProfileDao):
        self.dao_map[branch] = dao

    def get_dao(self, branch: str) -> BranchProfileDao:
        return self.dao_map[branch]
