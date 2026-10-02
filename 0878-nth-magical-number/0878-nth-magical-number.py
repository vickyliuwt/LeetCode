class Solution:
    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a % b)

    def lcm(self, a: int, b: int) -> int:
        return (a // self.gcd(a, b)) * b

    def noOfMultiples(self, val: int, a: int, b: int) -> int:
        lcmAB = self.lcm(a, b)
        return val // a + val // b - val // lcmAB

    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        M = 10**9 + 7
        start, end = 1, 10**18
        nthMagicNum = 0
        while start <= end:
            mid = start + (end - start) // 2
            if self.noOfMultiples(mid, a, b) >= n:
                nthMagicNum = mid
                end = mid - 1
            else:
                start = mid + 1
        return nthMagicNum % M