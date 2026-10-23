class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
  
        buckets = {}
        w = valueDiff + 1

        for i in range(len(nums)):
            m = nums[i] // w

            if m in buckets:
                return True
            
            if m + 1 in buckets and (buckets[m + 1] - nums[i]) <= valueDiff:
                return True
            
            if m - 1 in buckets and (nums[i] - buckets[m - 1]) <= valueDiff:
                return True

            buckets[m] = nums[i]

            if i >= indexDiff:
                del buckets[nums[(i - indexDiff)] // w]

        return False
