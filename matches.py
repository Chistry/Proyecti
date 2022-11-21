from stadium import Stadiums
from teams import Teams


class Matches:
    def __init__(self, name, sta_ID, date_hour):
        super().__init__(sta_ID, name)
        self.date_hour = date_hour
