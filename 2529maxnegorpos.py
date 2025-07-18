class Solution(object):
    def maximumCount(self, nums):
        neg , pos = 0,0
        for i in nums:
            if i < 0:
                neg+=1
            elif i > 0:
                pos+=1
        if neg > pos : return neg
        else: return pos
        """
        :type nums: List[int]
        :rtype: int
        """
        
