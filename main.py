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


def registrar():
    for key in info_teams:
        name = key["name"]
        group= key["group"]
        fifa_code= key["fifa_code"]
        equipo= Teams(name, group, fifa_code)
        Teams.equipos.append(equipo)

    for key in info_stadiums:
        sta_name= key["name"]
        location= key["location"]
        sta_ID= key["id"]
        Stadiums(sta_name, location, sta_ID)

    for key in info_matches:
        home_team= key["home_team"]
        away_team= key["away_team"]
        date_hour= key["date"]
        Matches(home_team, away_team, date_hour)

def mostrarequipos():
    for team in Teams.equipos:
        team.mostrar()





registrar()
mostrarequipos()
