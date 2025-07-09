class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        gaps = []
        gaps.append(startTime[0]-0)
        for i in range (1,len(startTime)):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])
        sliwind = sum(gaps[:k+1])
        resultant = sliwind
        for i in range(k+1,len(gaps)):
            sliwind = sliwind  -  gaps[i-(k+1)] + gaps[i]
            resultant = max(resultant,sliwind)
        return resultant

        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        
