class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        d={}
        for i in arr:
            if i not in d:
                d[i]=1 
            else:
                d[i]+=1 
        out=[]
        for i in d.values():
            out.append(i)
        print(out)
        return len(out)==len(set(out))
