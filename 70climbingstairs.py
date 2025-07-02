class Solution(object):
    def climbStairs(self, n):
        # if n<=2:
        #     return n
        # dp = [0] * (n+1)
        # dp[1] = 1
        # dp[2] = 2
        # for i in range (3,n+1):
        #     dp[i] = dp[i-1] + dp [i-2]
        # return dp[n]
        if n<=2:
            return n
        a,b = 1,2
        for i in range(3,n+1):
            a,b = b,a+b
        return b
        """
        :type n: int
        :rtype: int
        """
        
