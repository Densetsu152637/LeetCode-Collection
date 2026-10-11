# 1207. Unique Number of Occurrences
def uniqueOccurrences(arr: list[int]) -> bool:
    occ = dict()
    for val in arr:
        if occ.get(val) != None:
            occ[val] += 1
        else:
            occ[val] = 1
        
    values = list(occ.values())
    return len(set(values)) == len(values)