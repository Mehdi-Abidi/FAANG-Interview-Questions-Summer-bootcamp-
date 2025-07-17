class Solution(object):
    def maximumLength(self, nums, k):
        result = 0
        for i in xrange(k):
            dp = [0] * k
            for x in nums:
                dp[x % k] = dp[(i - x ) % k] + 1
            result = max(result, max(dp))
        return result
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
