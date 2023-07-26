class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i<j and nums[i]==nums[j]:
                    c+=1 
        return c
