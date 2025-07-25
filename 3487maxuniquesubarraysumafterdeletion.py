class Solution(object):
    def maxSum(self, nums):
        seen = set()
        sum1 = 0
        maxi = max(nums)
        if maxi < 0:
            return maxi
        for num in nums:
            if num not in seen:
                if num > 0:
                    seen.add(num)
                    sum1 +=num
        return sum1
        """
        :type nums: List[int]
        :rtype: int
        """
        
