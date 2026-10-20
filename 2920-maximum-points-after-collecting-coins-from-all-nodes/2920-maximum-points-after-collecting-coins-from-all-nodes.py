class Solution:
    def maximumPoints(self, edges: List[List[int]], A: List[int], k: int) -> int:
        n = len(edges) + 1
        G = [set() for i in range(n)]
        for i,j in edges:
            G[i].add(j)
            G[j].add(i)

        @cache
        def dp(i, pre, v):
            if v > 13:
                return 0
            a = A[i] >> v
            op1 = a - k + sum(dp(j, i, v) for j in G[i] if j != pre)
            if a >= k + k:
                return op1
            op2 = (a >> 1) + sum(dp(j, i, v + 1) for j in G[i] if j != pre)
            return max(op1, op2)

        return dp(0, -1, 0)