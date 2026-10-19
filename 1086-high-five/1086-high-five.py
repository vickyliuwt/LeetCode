class Solution(object):
    def highFive(self, items):
        d = {}

        for i, score in items:
            if i in d:
                d[i].append(score)
            else:
                d[i] = [score]

        res = []

        for i in d:
            d[i].sort()
            res.append([i, sum(d[i][-5:]) // 5])

        return sorted(res, key=lambda x: x[0])