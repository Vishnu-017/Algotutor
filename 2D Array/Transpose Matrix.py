class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        l=[]
        m=len(matrix)
        n=len(matrix[0])
        for i in range(n):
            temp=[]
            for j in range(m):
                #l[j][i]=matrix[i][j]
                #print(matrix[j][i])
                temp.append(matrix[j][i])
            l.append(temp)
        return l
