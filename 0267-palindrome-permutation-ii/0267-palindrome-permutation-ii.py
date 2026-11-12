class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
            counter = Counter(s)
            res = []
            
            def backtrack(cur=""):
                if not counter:
                    res.append(cur)
                    return
                for c in list(counter.keys()):
                    counter[c] -= 2
                    if not counter[c]:
                        del counter[c]
                    backtrack(c+cur+c)
                    counter[c] += 2

            oddCounts = [c for c in counter if counter[c]%2] # The characters in counter with odd count
            
            if not len(oddCounts): # if no odd chars, we can simply backtrack
                backtrack()
                
            if len(oddCounts) == 1: # if exactly one odd char, backtrack with oddChar in the middle of string
                oddChar = oddCounts[0]
                counter[oddChar] -= 1
                if not counter[oddChar]:
                    del counter[oddChar]
                backtrack(oddChar)
                
            return res