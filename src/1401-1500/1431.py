# 1431. Kids With the Greatest Number of Candies
def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    return_list = [False]*len(candies)
    max_candies = max(candies)
    
    for (i, cand) in enumerate(candies):
        if (cand + extraCandies >= max_candies):
            return_list[i] = True
            
    return return_list