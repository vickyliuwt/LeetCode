class Solution:                                            # L01
    def numSquares(self, n: int) -> int:                   # L02
        dp = [float('inf')] * (n + 1)                      # L03
        dp[0] = 0                                          # L04
        for i in range(1, n + 1):                          # L05
            j = 1                                          # L06
            while j * j <= i:                              # L07
                dp[i] = min(dp[i], dp[i - j * j] + 1)      # L08
                j += 1                                     # L09
        return dp[n]                                       # L10