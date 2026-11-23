class Solution:
    def minArea(self, image: List[List[str]], r: int, c: int) -> int:
        m, n = len(image), len(image[0])
        self.left = self.right = c
        self.top = self.bottom = r
        DIR = [0, 1, 0, -1, 0]
        
        def dfs(r, c):
            if r < 0 or r == m or c < 0 or c == n or image[r][c] == "0": return
            self.left = min(self.left, c)
            self.right = max(self.right, c)
            self.top = min(self.top, r)
            self.bottom = max(self.bottom, r)
            image[r][c] = "0"
            for i in range(4):
                dfs(r + DIR[i], c + DIR[i+1])
                
        dfs(r, c)
        return (self.bottom - self.top + 1) * (self.right - self.left + 1)