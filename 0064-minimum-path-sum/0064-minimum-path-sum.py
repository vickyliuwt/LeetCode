from functools import lru_cache          # lru_cache = 自动备忘录

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @lru_cache(maxsize=None)          # ← 加这一行，自动记忆化！
        def f(i, j):
            if i == 0 and j == 0: return grid[0][0]
            if i < 0 or j < 0:    return float('inf')
            return grid[i][j] + min(f(i - 1, j), f(i, j - 1))

        res = f(m - 1, n - 1)
        f.cache_clear()                   # 清缓存（避免测试之间互相污染）
        return res
        
        