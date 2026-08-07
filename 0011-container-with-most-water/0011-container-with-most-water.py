class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, best = 0, len(height) - 1, 0        # 技巧①：多重赋值
        while left < right:
            best = max(best, (right - left) * min(height[left], height[right]))  # 技巧②③
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return best