class Student:
    
    def __init__(self,name):
        self.name = name
    
    def calculate_avg(self,deta):
        sum = 0
    
        for num in deta:
            sum += num
        
        avg =sum/len(deta)
        return avg


    def judge(self,avg):
        
        if(avg >= 60):
            result="passed"
        else:
            result="failed"
        return result        

a001 = Student("sato")
deta = [70,65,50,10,30]
avg = a001.calculate_avg(deta)
result = a001.judge(avg)

print(avg)
print(a001.name+" "+result)        