class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_idx = -float('inf')
        word2_idx = -float('inf')
        min_dist = float('inf')
        
        for i, word in enumerate(wordsDict):
            if word == word1:
                word1_idx = i
                min_dist = min(min_dist, abs(word1_idx - word2_idx))
            elif word == word2:
                word2_idx = i
                min_dist = min(min_dist, abs(word1_idx - word2_idx))
        
        return min_dist