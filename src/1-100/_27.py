# 27. Remove Element
class Solution:
    
    def removeElement(self, nums: list[int], val: int) -> int:        
        n = len(nums)
        p = n - 1
        
        # iterate backwards, swapping elements with back items to replace found values
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[p], nums[i] = nums[i], nums[p]
                while nums[p] == val:
                    p -= 1
                
        # delete matched vals from end
        k = n - p - 1
        del nums[-k:]
        return k
    
    
    
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    Solution.removeElement(None, nums, 2)    
    print(nums)
