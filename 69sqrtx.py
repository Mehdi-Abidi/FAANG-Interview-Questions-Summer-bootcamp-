class Solution(object):
    def mySqrt(self, x):
        c = 2
        if x == 0 or x==1:
            return x  
        
        while c <= x:
            if c*c == x :
                return c

            elif c*c > x:
                return c-1
            else:
                c+=1  
        """
        :type x: int
        :rtype: int
        """
        
