class Solution(object):
    def maxEvents(self, events):
        events = sorted(events, key = lambda x: (x[0], x[1]))
        curr = events[0][0]
        eid = 0
        count = 0
        h = []
        while eid < len(events):
            if events[eid][0] <= curr:
                heappush(h, (events[eid][1],eid))
                eid += 1
            else:
                if h:
                    eend,x = heappop(h)
                    if curr <= eend:
                        count += 1
                        curr += 1
                else:
                    curr = events[eid][0]
        while h: 
            eend,x = heappop(h)
            if curr <= eend:
                count += 1
                curr += 1
        return count

        """
        :type events: List[List[int]]
        :rtype: int
        """
        
