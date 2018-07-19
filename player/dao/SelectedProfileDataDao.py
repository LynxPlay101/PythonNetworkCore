from typing import Tuple, List, MutableMapping

from player.profiles.SelectedProfileData import SelectedProfileData
from sql.GenericListDao import GenericListDao
from sql.SQLProvider import SQLProvider


def load_data(t: List[Tuple]) -> SelectedProfileData:
    data: MutableMapping[str, int] = {}
    for row in t:
        data[row[1]] = row[2]
    return SelectedProfileData(data)


class SelectedProfileDataDao(GenericListDao[SelectedProfileData]):

    def __init__(self, provider: SQLProvider):
        super().__init__(provider, "selected_profile", [["uuid", "_binary %s"], ["branch", "%s"]]
                         , lambda t: load_data(t))
        pass
