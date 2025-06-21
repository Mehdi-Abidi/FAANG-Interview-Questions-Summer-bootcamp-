class Solution(object):
    def minRemoveToMakeValid(self, s):
        # stack = []
        # st = list(s)
        # for i in range(len(st)):
        #     if st[i]=='(':
        #         stack.append(i)
        #     if st[i]==')':
        #         if stack:
        #             stack.pop()
        #         else:
        #             st[i]=''
        # while stack:
        #     index = stack.pop()
        #     st[index]=''
        # return ''.join(st)
        s = list(s)
        c = 0
        for i in range(len(s)):
            if s[i]=='(':
                c = c + 1
            elif s[i]==')':
                if c :
                    c = c - 1
                else:
                    s[i]=''
        x = len(s) - 1
        while x >=0 and c:
            if s[x] == '(':
                s[x] = ''
                c = c-1
            x = x - 1
            
        return ''.join(s)   
        """
        :type s: str
        :rtype: str
        """
        
