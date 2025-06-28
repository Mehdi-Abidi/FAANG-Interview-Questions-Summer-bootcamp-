class Solution(object):
    def lengthOfLastWord(self, s):
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]!=' ':
                c+=1
            elif c>0:
                return c
        return c
        """
        :type s: str
        :rtype: int
        """
        
