class StudentReport :
    def __init__(self,name,marks:list):
        self.name = name 
        self.marks = marks
    def average_mark(self):
        total = 0
        no_of_subjects = 0
        for mark in self.marks:
            total += mark
            no_of_subjects += 1
        
        return total / no_of_subjects
    def maximum_mark(self):
        max_marks = self.marks[0]
        for mark in self.marks:
            if mark > max_marks:
                max_marks = mark
        
        return max_marks
    def result(self):
        if self.average_mark() >= 40:
            return "Pass"
        else:
            return  "fail"
    def display(self):
        print(f"{self.name}'s average mark : {self.average_mark()},maximum mark : {self.maximum_mark()},result : {self.result()}")
s1 = StudentReport("Hareesh Reddy",[40,50,99])
s1.display()
