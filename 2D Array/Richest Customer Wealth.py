class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        t=0
        for i in accounts:
            m=sum(i)
            if(m>t):
                t=m
        return t
