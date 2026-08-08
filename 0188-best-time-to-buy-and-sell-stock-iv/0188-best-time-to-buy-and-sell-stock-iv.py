class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        if k >= n // 2:
            total = 0
            for i in range(n - 1):
                if prices[i + 1] > prices[i]:
                    total += prices[i + 1] - prices[i]
            return total
        buy = [float('-inf')] * (k + 1)
        sell = [0] * (k + 1)
        for p in prices:
            for j in range(1, k + 1):
                buy[j] = max(buy[j], sell[j - 1] - p)
                sell[j] = max(sell[j], buy[j] + p)
        return sell[k]