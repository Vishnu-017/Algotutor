class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        l=[]
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]<0:
                    l.append(grid[i][j])
        print(l)
        return len(l)
