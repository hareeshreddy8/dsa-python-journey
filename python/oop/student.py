class Student :
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks
    def details(self):
        print(f"{self.name}  {self.marks}")
    
    def is_pass(self):
        if self.marks >= 40 :
            print(f"{self.name} is pass")
        else:
            print(f"{self.name} is fail")
s1 = Student("hareesh",90)
s1.details()
s1.is_pass()