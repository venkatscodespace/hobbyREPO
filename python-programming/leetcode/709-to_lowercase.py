def isASCII(s0):
    try:
        s0.decode("ASCII")
        return True
    except UnicodeDecodeError:
        return False
class Solution(object):
    def toLowerCase(self, s1):
        if (1 <= len(s1) <= 100) and (isASCII(s1)==True):
            return s1.lower()
