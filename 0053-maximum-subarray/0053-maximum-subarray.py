class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = cur = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            cur = max(x, cur + x)
            best = max(best, cur)
        return best