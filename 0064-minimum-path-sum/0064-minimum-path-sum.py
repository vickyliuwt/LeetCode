class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}

        def f(i, j):
            if i == 0 and j == 0:
                return grid[0][0]
            if i < 0 or j < 0:
                return float('inf')
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i, j)] = grid[i][j] + min(f(i - 1, j), f(i, j - 1))
            return memo[(i, j)]
        return f(m - 1, n - 1)

        
        