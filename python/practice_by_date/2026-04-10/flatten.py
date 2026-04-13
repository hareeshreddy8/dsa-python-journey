def flatten(nested:list):
    result = []
    for item in nested:
        if isinstance(item,list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result