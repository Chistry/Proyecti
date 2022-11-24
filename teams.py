class Teams:
    nombres= []
    equipos= []

    def __init__(self, name, group, fifa_code):
        self.name = name
        self.group = group
        self.fifa_code = fifa_code
    
    def mostrar(self): 
        print (f'Name: {self.name} \nGroup: {self.group} \nFIFA code: {self.fifa_code}\n \n')

    def buscarequipospornombres(x):
        def lineal_search(pais,x):
            for n in x:
                if pais == n:
                    return pais
        pais= input("Please enter a country: ")
        tO= lineal_search(pais,x)
        if lineal_search(pais, x):
            print (tO.mostrar())
            
        else:
            print("The country", tO,"is not present")
    
