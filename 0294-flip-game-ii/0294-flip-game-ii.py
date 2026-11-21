class Solution:
    def canWin(self, s: str) -> bool:

        def dfs(state):
            arr = list(state)
            n = len(arr)

            for i in range(n-1):
                if arr[i] == '+' and arr[i+1] == '+':
                    arr[i],arr[i+1] = '-','-'
                    next_state = ''.join(arr)

                    if not dfs(next_state):
                        arr[i],arr[i+1] = '+','+'
                        return True

                    arr[i],arr[i+1] = '+','+'

            return False

        return dfs(s)