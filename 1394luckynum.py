class Solution(object):
    def findLucky(self, arr):
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        result a= -1
        for num in freq:
            if num == freq[num]:
                result = max(result, num)
        
        return result
        """
        :type arr: List[int]
        :rtype: int
        """
        
