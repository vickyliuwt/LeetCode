class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        prefix = [ list(accumulate(row)) for row in matrix ]
        self.prefix = prefix
        self.matrix = matrix

    def update(self, i1: int, j1: int, val: int) -> None:
        self.prefix[i1][j1:] = [ x + (val - self.matrix[i1][j1]) for x in self.prefix[i1][j1:] ]
        self.matrix[i1][j1] = val
        return


    def sumRegion(self, i1: int, j1: int, i2: int, j2: int) -> int:        
        sm = 0

        for i in range(i1, i2+1):
            sm +=        self.prefix[i][j2] - self.prefix[i][j1-1] if j1-1 >= 0 \
                    else self.prefix[i][j2]

        return sm 