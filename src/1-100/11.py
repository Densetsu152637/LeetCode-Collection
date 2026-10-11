# 11. Container With Most Water
def maxArea(self, height: list[int]) -> int:
    
    left: int = 0
    right: int = len(height) - 1
    right_bigger: str
    max_area: int = 0
    area: int = 0
    
    while left < right:
        if height[left] < height[right]:
            right_bigger = True
        else:
            right_bigger = False
            
        area = (right-left)*min(height[left], height[right])
        
        if (area > max_area):
            max_area = area
            
        if (right_bigger):
            left += 1
        else:
            right -= 1
            
            
    return max_area