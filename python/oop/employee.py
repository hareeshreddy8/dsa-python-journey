class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def increase_salary(self,percentage:float):
        self.salary += self.salary * (percentage / 100)
        return self.salary
    
    def display(self):
        print(f"{self.name}'s salary : {self.salary}")
    
e1 = Employee("Hareesh",100000)
e1.increase_salary(30.00)
e1.display()