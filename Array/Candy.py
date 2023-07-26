class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        dp=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if dp[i]<=dp[i-1] and ratings[i]>ratings[i-1]:
                dp[i]=dp[i-1]+1 
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1] and dp[i]<=dp[i+1]:
                dp[i]=dp[i+1]+1 
        return sum(dp)
