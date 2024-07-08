class Solution(object):
    # Define a class named Solution
    def lengthOfLastWord(self, s):
        # Define a method lengthOfLastWord that takes a parameter s
        list_s = s.split()
        # Split the string s into a list of words based on whitespace
        return len(list_s[-1])
        # Return the length of the last word in the list list_s