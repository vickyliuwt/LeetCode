class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        l = len(s)
        ans = 0
        while l > 1:
            l -= 1
            f = int(s[0])          # leading digit
            s = s[1:]              # remaining digits
            ans += f * l * (10 ** (l - 1))   # ones from f full blocks
            if f == 0:
                continue
            if f == 1:
                ans += int(s) + 1  # leading 1 appears in [1000..1xxx]
            else:
                ans += 10 ** l     # whole block [1000..1999] is covered
        ans += (0 if s == '0' else 1)  # last digit: 1 if d >= 1
        return ans