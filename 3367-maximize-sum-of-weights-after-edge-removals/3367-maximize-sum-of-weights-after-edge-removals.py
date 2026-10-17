class Solution:
    def maximizeSumOfWeights(self, edges: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        G = [[] for i in range(n)]
        for i,j,w in edges:
            G[i].append([j, w])
            G[j].append([i, w])

        def dfs(i, pre = -1):
            res = 0
            diff = []
            for j, w in G[i]:
                if j == pre: continue
                v1, v2 = dfs(j, i)
                res += v2
                diff.append(max(0, v1 + w - v2))
            return res + sum(nlargest(k - 1, diff)), res + sum(nlargest(k, diff))

        return dfs(0)[1]