class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums2 = sorted(nums1[:m]+nums2[:n])
        nums1[:] = nums2
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
