class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):            # 只扫一遍 nums
            ans[i] = nums[i]          # 前半段
            ans[i + n] = nums[i]      # 后半段
        return ans