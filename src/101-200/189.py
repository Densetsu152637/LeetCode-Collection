# 189. Rotate Array
def reverse(arr, start, finish):    
    while start < finish:
        arr[start], arr[finish] = arr[finish], arr[start]
        start += 1
        finish -= 1

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        
        n = len(nums)
        k %= n
        # reverse entire array
        reverse(nums, 0, n - 1)
        # reverse first k items
        reverse(nums, 0, k - 1)
        # reverse last n - k items
        reverse(nums, k, n - 1)
        
        
        