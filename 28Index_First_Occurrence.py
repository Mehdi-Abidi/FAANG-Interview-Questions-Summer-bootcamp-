class Solution(object):
    def strStr(self, haystack, needle):
        idx = -1
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i + len(needle)]==needle:
                idx= i
                break
        return idx
        # return haystack.find(needle)
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
