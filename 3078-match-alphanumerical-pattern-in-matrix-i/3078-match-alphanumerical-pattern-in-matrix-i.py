class Solution:
    def findPattern(self, board: List[List[int]], pattern: List[str]) -> List[int]:
        # Bruteforce?

        m = len(board)
        n = len(board[0])

        a = len(pattern)
        b = len(pattern[0])

        for i in range(m-a+1):
            for j in range(n-b+1):
                print(i, j)
                flag = True
                hm = dict()
                for k in range(a):
                    if not flag:
                        break
                    for l in range(b):
                        if pattern[k][l].isdigit():
                            if int(pattern[k][l]) != board[i+k][j+l]:
                                flag = False
                                break
                        else:
                            if pattern[k][l] not in hm:
                                hm[pattern[k][l]] = board[i+k][j+l]
                            else:
                                if hm[pattern[k][l]] != board[i+k][j+l]:
                                    flag = False
                                    break
                hs = set()
                for key in hm.keys():
                    hs.add(hm[key])
                
                if len(hm) != len(hs):
                    flag = False
                
                if flag:
                    return [i, j]
        
        return [-1, -1]