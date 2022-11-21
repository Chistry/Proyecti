class Teams:
    equipos= []
    nombres= []
    def __init__(self, name, group, fifa_code):
        self.name = name
        self.group = group
        self.fifa_code = fifa_code
    
    def mostrar(self): 
        print (f'Name: {self.name} \nGroup: {self.group} \nFIFA code: {self.fifa_code}\n \n')
