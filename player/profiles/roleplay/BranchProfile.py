class BranchProfile:
    pass


class HogwartsProfile(BranchProfile):
    house: str
    year: int

    def __init__(self, house: str, year: int):
        self.year = year
        self.house = house
        pass

    pass


class MordoniaProfile(BranchProfile):
    kingdom: str
    job: str

    def __init__(self, kingdom: str, job: str):
        self.job = job
        self.kingdom = kingdom
        pass

    pass
