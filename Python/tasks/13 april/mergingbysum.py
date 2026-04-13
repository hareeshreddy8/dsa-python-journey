def merging_bysum(d1:dict,d2:dict):
    merged_dict = {}
    # for k in d1.keys()|d2.keys():
    #     merged_dict[k] = d1.get(k,0) + d2.get(k,0)
    for k in d1.keys():
        if k in d2.keys():
            merged_dict[k] = d1.get(k,0) + d2.get(k,0)

        else:
            merged_dict[k] = d1.get(k,0)

    for k in d2.keys():
        if k not in merged_dict:
            merged_dict[k]  = d2.get(k,0)
    return merged_dict
    
d1 = {"a":1, "b":2}
d2 = {"a":3, "c":4}
print(merging_bysum(d1,d2))