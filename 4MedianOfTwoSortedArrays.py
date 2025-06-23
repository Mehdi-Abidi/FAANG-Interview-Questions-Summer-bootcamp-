class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        temp = sorted(nums1 + nums2)
        length = len(temp)
        if length % 2 != 0:
            return temp[length // 2]
        else:
            return float((temp[length//2-1]+temp[length//2])/2.0)
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
