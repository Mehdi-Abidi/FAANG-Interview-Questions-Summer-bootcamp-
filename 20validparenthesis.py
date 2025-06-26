class Solution(object):
    def isValid(self, s):
        maps = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in maps:
                if not stack or stack[-1]!=maps[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return not stack
            

        """
        :type s: str
        :rtype: bool
        """
        
