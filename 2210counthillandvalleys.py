class Solution(object):
    def countHillValley(self, nums):
        n = len(nums)
        i = 0
        j = 1
        count = 0
        while(j+1 < n):
            if (nums[i]< nums[j] and nums[j] > nums[j+1]) or (nums[i] > nums[j] and nums[j] < nums[j+1]):
                count+=1
                i = j
            j+=1
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        
