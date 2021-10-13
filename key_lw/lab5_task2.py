class Rectangle:
    def __init__(length,width,name):
        self.length=length
        self.width=width
        self.name=name
        
    def get_area(self):
        return self.length*self.width
    
    def compare_size(self,other):
        if self.get_area<other.get_area:
            print(other.name,"is larger")
        else:
            print(self.name,"is larger")

R1=Rectangle(1,2,"R1")
R2=Rectangle(1,3,"R2")
compare_size(R1,R2)



