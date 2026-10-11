# 2390. Removing Stars From a String
def removeStars(s: str) -> str:
    r_a = []
    for char in s:
        if char == "*":
            r_a.pop()
        else:
            r_a.append(char)    
            
    return "".join(r_a) 