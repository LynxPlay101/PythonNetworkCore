from typing import MutableMapping


class SelectedProfileData:
    selected_profiles: MutableMapping[str, int]

    def __init__(self, selected_profiles: MutableMapping[str, int]):
        self.selected_profiles = selected_profiles
        pass

    def get_profile(self, branch: str) -> int:
        return self.selected_profiles.get(branch)

    def set_profile(self, branch: str, profile_id: int):
        self.selected_profiles[branch] = profile_id
