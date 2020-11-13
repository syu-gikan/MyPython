class Stundent:
    
    def __init__(self,name):
        self.name = name
    
    def avg(self,math,english):
        print((math + english) /2)
        
a001 = Stundent("sato")
print(a001.name)

a002 = Stundent("tanaka")
print(a002.name)
