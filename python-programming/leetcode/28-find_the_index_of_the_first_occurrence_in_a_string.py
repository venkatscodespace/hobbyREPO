class Solution(object):
    def strStr(self, haystack, needle):
        if (1 <= len(haystack)) and ((len(needle) <= 104)):
            haystack=haystack.lower()
            needle=needle.lower()
            if needle in haystack:
                return haystack.index(needle)
            else:
                return -1
