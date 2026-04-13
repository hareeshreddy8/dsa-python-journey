from typing import Dict
def MergingDicts(d1 : dict,d2 : dict):
    merged_dict = {}
    # for key in d1:
    #     if key in d2:
    #         merged_dict[key] = d1[key] + d2[key]

    #     else :
    #         merged_dict[key] = d1[key]

    # for key in d2 :
    #     if key not in merged_dict:
    #         merged_dict[key] = d2[key]
    for key in d1.keys() | d2.keys():
        merged_dict[key] = d1.get(key,0) + d2.get(key,0)

    # comprehension
    merged ={k : d1.get(k,0) + d2.get(k,0) for k in d1.keys()|d2.keys()}
    return merged_dict
d1 = {"a": 2, "b": 3}
d2 = {"a": 1, "c": 4}
print(MergingDicts(d1,d2))
