# 1679. Max Number of K-Sum Pairs TODO
def maxOperations(self, nums: list[int], k: int) -> int:
    nums.sort()
    left = 0
    right = len(nums) - 1
    while left < right:
        pass