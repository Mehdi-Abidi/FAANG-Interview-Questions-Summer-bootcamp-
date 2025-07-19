class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort()
        res = [folder[0]]
        for path in folder[1:]:
            if not path.startswith(res[-1] + '/'):
                res.append(path)
        return res
        """
        :type folder: List[str]
        :rtype: List[str]
        """
        
