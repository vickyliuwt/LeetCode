class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def pieces_needed(cap: int) -> int:
            count, cur = 1, 0
            for x in nums:
                if cur + x > cap:  
                    count += 1
                    cur = x 
                else:
                    cur += x
            return count

        lo, hi = max(nums), sum(nums) 
        while lo < hi:                 # 区间收缩到一点
            mid = (lo + hi) // 2       # 向下取整的中点
            if pieces_needed(mid) <= k:
                hi = mid               # 可行 → 保留 mid，往小的方向找
            else:
                lo = mid + 1           # 不可行 → mid 及以下作废
        return lo