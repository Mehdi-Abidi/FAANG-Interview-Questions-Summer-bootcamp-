class Solution(object):
    def maximumGain(self, s, x, y):
        stack = []
        score = 0
        if x > y:
            a, b, px, py = 'a', 'b', x, y
        else:
            a, b, px, py = 'b', 'a', y, x

        for ch in s:
            if stack and stack[-1] == a and ch == b:
                stack.pop()
                score += px
            else:
                stack.append(ch)

        new_stack = []
        for ch in stack:
            if new_stack and new_stack[-1] == b and ch == a:
                new_stack.pop()
                score += py
            else:
                new_stack.append(ch)

        return score
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        
