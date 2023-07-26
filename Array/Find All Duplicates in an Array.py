class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        res=[]
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1 
            else:
                d[nums[i]]+=1 
        for k,v in d.items():
            if v==2 :
                res.append(k)
        
                
        print(res)
        return (res)
