class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        n = len(s)
        counter = collections.Counter(s)
        
        def helper(tmp):
            if len(tmp) == n:
                ans.append(tmp)
                return 
            for k, v in counter.items():
                if v > 0:
                    counter[k] -= 2
                    helper(k + tmp + k)
                    counter[k] += 2
        
        odd = [key for key, value in counter.items() if value % 2 != 0]
        if len(odd) > 1:
            return []
        if len(odd) == 1:
            counter[odd[0]] -= 1
            helper(odd[0])
        else:
            helper('')
        return ans