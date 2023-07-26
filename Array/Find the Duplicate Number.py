class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i not in d:
                d[i]=1 
            else:
                d[i]+=1 
        print(d)
        for i in d.keys():
            if d[i]>1:
                return i
