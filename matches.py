from stadium import Stadiums
from teams import Teams

class Matches:
    lista_partidos=[]
    def __init__(self, date_hour, sta_id, home_team, away_team):
        self.date_hour = date_hour
        self.sta_id = sta_id
        self.home_team = home_team #No tiene el objeto es un string
        self.away_team = away_team

    def mostrar(self): 
        print (f'Hour: {self.date_hour} \nStadium ID: {self.sta_id} \nHome team code: {self.home_team}\nAway team: {self.away_team} \n')


