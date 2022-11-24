import requests
from teams import Teams
from stadium import Stadiums
from matches import Matches

url_teams= 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json'
r_teams = requests.get(url_teams)
info_teams = r_teams.json()

url_stadiums= 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json'
r_stadiums= requests.get(url_stadiums)
info_stadiums= r_stadiums.json()

url_matches= 'https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json'
r_matches= requests.get(url_matches)
info_matches= r_matches.json()

#Registra la informacion necesaria de los jsons
def registrar():
    for key in info_teams:
        name = key["name"]
        group= key["group"]
        fifa_code= key["fifa_code"]
        equipos= Teams(name, group, fifa_code)
        Teams.equipos.append(equipos)
        Teams.nombres.append(name)

    for key in info_stadiums:
        sta_name= key["name"]
        location= key["location"]
        sta_ID= key["id"]
        Stadiums(sta_name, location, sta_ID)

    for key in info_matches:
        home_team= key["home_team"]
        away_team= key["away_team"]
        date_hour= key["date"]
        sta_ID= key["stadium_id"]
        partidos = Matches(date_hour, sta_ID, home_team, away_team)
        Matches.lista_partidos.append(partidos)


def mostrarequipos():
    for team in Teams.equipos:
        team.mostrar()

def mostrarpartido():
    for team in Matches.lista_partidos:
        Teams.buscarequipospornombres(Matches.lista_partidos)

def main():
    #Teams.buscarequipospornombres(Teams.nombres)
    #Teams.buscarequipospornombres(Matches.lista_partidos)
    x=1






registrar()
mostrarpartido()


