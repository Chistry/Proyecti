class Stadiums:
    prueba= []
    def __init__(self, sta_name, location, sta_ID):
        self.sta_name = sta_name
        self.location = location
        self.sta_ID = sta_ID
    
    def mostrar(self): 
        print (f'Name: {self.sta_name} \nGroup: {self.location} \nFIFA code: {self.sta_ID} \n')