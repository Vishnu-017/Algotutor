class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d={}
        for r,row in enumerate(matrix):
            for c,col in enumerate(row):
                if r-c not in d:
                    d[r-c]=col
                elif d[r-c] != col:
                    return False
        return True
        
