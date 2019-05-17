class People:
    name = "" #property 
    age = 0
    country = ""

    def __init__(self,name,age,country): # it's the constructor 
        self.name = name
        self.age = age
        self.country = country

    #self is equals to "this" in other languages 
    def saludar(self):
        print("my name is ", self.name) # methods
    
    def despedir(self):
        print("Good Bye ", self.name)

Alex = People("Alex",25,"Usa")

print (Alex.name,Alex.age,Alex.country)
Alex.saludar()
Alex.despedir()