class Solution(object):
    def trailingZeroes(self, n):
        count=0
        i=5
        while (n/i)>=1:
            count+=(n/i)
            i*=5
        return count
