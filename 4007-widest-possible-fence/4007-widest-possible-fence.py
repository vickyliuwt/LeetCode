class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        cnt = {}
        for h in planks:
            cnt[h] = cnt.get(h, 0) + 1
        vals = sorted(cnt)
        pair = {}
        for i in range(len(vals)):
            a = vals[i]
            if cnt[a] >= 2:
                s = a + a
                pair[s] = pair.get(s, 0) + cnt[a] // 2
            for j in range(i + 1, len(vals)):
                b = vals[j]
                s = a + b
                pair[s] = pair.get(s, 0) + min(cnt[a], cnt[b])
        best = 0
        for h in cnt:
            if cnt[h] > best:
                best = cnt[h]
        for s in pair:
            tot = pair[s] + cnt.get(s, 0) 
            if tot > best:
                best = tot
        return best