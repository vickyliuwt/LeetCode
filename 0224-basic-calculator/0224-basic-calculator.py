class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res, num, sign = 0, 0, 1        # 一行同时赋 3 个变量（Python 语法糖）
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                res += sign * num; num = 0; sign = 1
            elif ch == '-':
                res += sign * num; num = 0; sign = -1
            elif ch == '(':
                stack.append(res); stack.append(sign); res = 0; sign = 1
            elif ch == ')':
                res += sign * num; num = 0
                res = res * stack.pop()
                res = res + stack.pop()
                sign = 1
        return res + sign * num