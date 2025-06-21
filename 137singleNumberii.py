class Solution(object):
    def singleNumber(self, nums):
        frq = {}
        for num in nums:
            if num in frq:
                frq[num]+=1
            else:
                frq[num]=1
        for i,c in frq.items():
            if c == 1:
                return i
        # return ((sum(set(nums))*3)-sum(nums))//2
        """
        :type nums: List[int]
        :rtype: int
        """
        
