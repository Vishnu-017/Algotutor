class Solution(object):
    def maxScore(self,cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        
        max_score,curr_score, n= 0,0, len(cardPoints)
        total_score=sum(cardPoints)
        if n == k:
            return total_score
        for i in range(n-k-1):
            curr_score += cardPoints[i]
        print(curr_score)
        for i in range(n-k-1, n):
            curr_score += cardPoints[i]
            max_score = max(max_score, total_score - curr_score)
            curr_score -= cardPoints[i-(n-k-1)] 
        return max_score
