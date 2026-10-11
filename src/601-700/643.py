# 643. Maximum Average Subarray I
def findMaxAverage(self, nums: list[int], k: int) -> float:
    if len(nums) < k:
        return sum(nums)/k
    elif len(nums) == k:
        return sum(nums)/k
    
    sums = [0]*(len(nums) - k + 1)
    sums[0] =  sum(nums[0:k])
    
    for i in range(1, len(nums) - k + 1):
        sums[i] = sums[i-1] - nums[i-1] + nums[i+k-1]
                    
    return max(sums)/k