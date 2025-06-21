class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last_occ = {char:i for i,char in enumerate(s)}
        visited = set()
        stack = []
        for i,c in enumerate(s):
            if c in visited :
                continue
            while stack and last_occ[stack[-1]]>i and c < stack[-1]:
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return ''.join(stack)
