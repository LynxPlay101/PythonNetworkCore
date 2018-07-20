from typing import List, Callable, Tuple, Optional

from player.profiles.roleplay.BranchProfile import HogwartsProfile, BranchProfile, MordoniaProfile
from sql.GenericDao import GenericDao, T
from sql.SQLProvider import SQLProvider


class BranchProfileDao(GenericDao[BranchProfile]):

    def __init__(self, provider: SQLProvider, table: str, key: List[List[str]], mapper: Callable[[Tuple], T]):
        super().__init__(provider, table, key, mapper)

    def lookup(self, key: List) -> Optional[T]:
        return super().lookup(key)


class HogwartsProfileDao(BranchProfileDao):

    def __init__(self, provider: SQLProvider):
        super().__init__(provider, "hogwarts_profile", [["profile_id", "%s"]], lambda c: self.build_profile(c))
        pass

    def lookup(self, key: List) -> Optional[T]:
        return super().lookup(key)

    def build_profile(self, t: Tuple) -> HogwartsProfile:
        return HogwartsProfile(t[1], t[2])

    pass


class MordoniaProfileDao(BranchProfileDao):

    def __init__(self, provider: SQLProvider):
        super().__init__(provider, "mordonia_profile", [["profile_id", "%s"]], lambda c: self.build_profile(c))
        pass

    def lookup(self, key: List) -> Optional[T]:
        return super().lookup(key)

    def build_profile(self, t: Tuple) -> MordoniaProfile:
        return MordoniaProfile(t[1], t[2])

    pass
