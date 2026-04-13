def CustomSort(students):
    sorted_marks = sorted(students,key = lambda x:(-x[1],x[0]))