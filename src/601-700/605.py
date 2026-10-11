# 605. Can Place Flowers
def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
    
    count: int = 0
    i: int = 0
    
    while i < len(flowerbed):
        try:
            if (flowerbed[i] == 0 and flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
                i += 2
            elif (flowerbed[i] == 1 and flowerbed[i+1] == 0):
                i += 2
            elif (flowerbed[i+1] == 1):
                i += 3
                
        except IndexError:
            if (flowerbed[i] == 0):
                flowerbed[i] = 1
                count += 1
            break
                
    return count >= n