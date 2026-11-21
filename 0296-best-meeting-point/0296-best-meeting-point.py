class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        # [1] collect sorted indices/coords for each dimension
        xs = [i for i in range(m) for j in range(n) if grid[i][j] == 1]
        ys = [j for j in range(n) for i in range(m) if grid[i][j] == 1]
        
        # [2] extraction of median value is trivial
        x = xs[len(xs)//2]
        y = ys[len(ys)//2]

        # [3] compute sum of distances between each point and meeting point;
        #    note that, for Manhattan distance, the final result is the  
        #    sum of individual distances for each dimension
        return sum(map(lambda xx: abs(xx-x), xs)) + \
             sum(map(lambda yy: abs(yy-y), ys))
