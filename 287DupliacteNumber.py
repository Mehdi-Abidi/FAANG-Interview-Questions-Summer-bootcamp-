class Solution(object):
    def findDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return i
            seen.add(i)
        # left = nums[0]
        # right = nums[0]
        # while True:
        #     left = nums[left]
        #     right = nums[nums[right]]
        #     if left == right:
        #         break
        # left = nums[0]
        # while left != right:
        #     left = nums[left]
        #     right = nums[right]
        # return left 
        """
        :type nums: List[int]
        :rtype: int
        """
  
