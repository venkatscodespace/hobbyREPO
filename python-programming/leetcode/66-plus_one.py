class Solution(object):
    def plusOne(self, digits):
        n=""
        L=[]
        if 1 <= len(digits) <= 100:
            for i in digits:
                if 0 <= i <= 9:
                    n+=str(i)
            x=int(n)+1
            for j in str(x):
                L.append(int(j))
            return L
