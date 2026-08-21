from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是较短的数组，防止 j 越界 + 优化复杂度
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        half = (m + n + 1) // 2          # 左半边应该装几个数
        lo, hi = 0, m                    # 在 [0, m] 里二分「切几个」

        while lo <= hi:
            i = (lo + hi) // 2           # nums1 左半拿 i 个
            j = half - i                 # nums2 左半自动拿 j 个

            maxLeft1  = nums1[i - 1] if i > 0 else float('-inf')
            minRight1 = nums1[i]     if i < m else float('inf')
            maxLeft2  = nums2[j - 1] if j > 0 else float('-inf')
            minRight2 = nums2[j]     if j < n else float('inf')

            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if (m + n) % 2 == 1:
                    return float(max(maxLeft1, maxLeft2))
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
            elif maxLeft1 > minRight2:
                hi = i - 1               # nums1 左半拿多了
            else:
                lo = i + 1               # nums1 左半拿少了

        return 0.0