# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        
        left[0] = nums[0]
        right[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            left[i] = nums[i] * left[i - 1]
            
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i] * right[i + 1]
            
        ret = [1] * len(nums)
        
        ret[0] = right[1]
        ret[-1] = left[-2]
        
        for i in range(1, len(nums) - 1):
            ret[i] = left[i - 1] * right[i + 1]
            
        return ret