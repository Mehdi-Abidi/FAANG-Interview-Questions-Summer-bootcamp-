class Solution(object):
    def twoSum(self, nums, target):
        # ls = []
        # temp = 0
        # for i in range(len(nums)):
        #     temp = nums[i]
        #     for j in range(i+1,len(nums)):
        #         temp+=nums[j]
        #         if(temp==target):
        #             ls.append(i)
        #             ls.append(j)
        #         temp-=nums[j]
        # return ls
        ls = {}
        temp = []
        for i in range (len(nums)):
            val = target - nums[i]
            if val in ls:
                temp.append(ls[val])
                temp.append(i)
                return temp
            ls[nums[i]] = i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
