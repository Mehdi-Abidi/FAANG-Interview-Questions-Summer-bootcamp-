class Solution(object):
    def romanToInt(self, s):
        smap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        val = 0
        for i in range(len(s)-1):
            if smap[s[i]] < smap[s[i+1]]:
                val-=smap[s[i]]
            else:
                val+=smap[s[i]]
        val+=smap[s[-1]]
        return val
        """
        :type s: str
        :rtype: int
        """
        
