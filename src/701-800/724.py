# 724. Find Pivot Index
def pivotIndex(nums: list[int]) -> int:
    
    left_side = [0]*len(nums)
    left_side[0] = nums[0]
    right_side = [0]*len(nums)
    right_side[-1] = nums[-1]
    
    for i in range(1, len(nums)):
        left_side[i] = left_side[i-1] + nums[i]
        right_side[-i-1] = right_side[-i] + nums[-i-1]
        
    for i in range(len(nums)):
        if left_side[i] == right_side[i]:
            return i
        
    return -1