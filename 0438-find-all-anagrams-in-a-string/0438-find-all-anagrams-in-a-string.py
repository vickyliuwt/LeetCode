class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        n, m = len(s), len(p)
        if m > n:
            return result
        p_count = Counter(p)
        window = Counter(s[:m])
        if window == p_count:
            result.append(0)
        for i in range(m, n):
            window[s[i]] += 1
            window[s[i - m]] -= 1
            if window[s[i - m]] == 0:
                del window[s[i - m]]
            if window == p_count:
                result.append(i - m + 1)
        return result
        