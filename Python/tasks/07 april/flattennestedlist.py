def FlattenNestedList(nested):
    result = []
    for nest in nested :
        for elements in nest :
            result.append(elements)

    return result 

nested = [[1,2],[3,4],[5]]
print(FlattenNestedList(nested))
def FlattenNest(nested):
    result = [element for nest in nested for element in nest]

    return result 
print(FlattenNest(nested))