class Solution(object):
    def maximumLength(self, nums):
        odd, even, alt, prev = 0, 0, 1, nums[0] % 2
        if prev:
            odd += 1
        else:
            even += 1

        for num in nums[1:]:
            curr = num % 2
            if curr:
                odd += 1
            else:
                even += 1
            if curr != prev:
                alt += 1
                prev = curr

        return max(odd, even, alt)
        
