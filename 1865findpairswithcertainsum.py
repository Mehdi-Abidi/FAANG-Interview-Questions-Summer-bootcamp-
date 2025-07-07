class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq2 = {}
        
        for num in nums2:
            if num in self.freq2:
                self.freq2[num] += 1
            else:
                self.freq2[num] = 1
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        old_val = self.nums2[index]
        new_val = old_val + val
        self.nums2[index] = new_val
        self.freq2[old_val] -= 1
        if self.freq2[old_val] == 0:
            del self.freq2[old_val]
        
        if new_val in self.freq2:
            self.freq2[new_val] += 1
        else:
            self.freq2[new_val] = 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        count = 0
        for num1 in self.nums1:
            target = tot - num1
            if target in self.freq2:
                count += self.freq2[target]
        return count


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
