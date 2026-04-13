def SimpleTransform(data):
    transformed_map = {}
    for tuple in data :
        if tuple not in transformed_map:
            transformed_map[tuple[0]] = tuple[1]

        else :
            transformed_map[tuple[0]] += tuple[1]

    return transformed_map