# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        l = 0
        r = len(numbers) - 1
        
        while l < r:
            
            s = numbers[l] + numbers[r]
            
            # hit
            if s == target:
                return [l + 1, r + 1]
            
            # low
            if s < target:
                l += 1
                
            # high
            if s > target:
                r -= 1
        
        
if __name__ == "__main__":
    numbers = [-5,-3,0,2,4,6,8]
    target = 5
    print(Solution.twoSum(None, numbers, target))