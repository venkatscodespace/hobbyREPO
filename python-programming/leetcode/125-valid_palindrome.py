class Solution(object):
    # Define a method 'isPalindrome' that takes a string 's' as an argument
    def isPalindrome(self, s):
        try:
            # Attempt to decode the string 's' to ASCII to ensure it contains only valid ASCII characters
            s.decode('ascii')
            # Check if the length of 's' is between 1 and 200,000 inclusive
            if (len(s) >= 1) and (len(s) <= 2 * (10 ** 5)):
                # Initialize an empty string 'str1' to store alphanumeric characters from 's'
                str1 = ""
                # Iterate through each character 'i' in the string 's'
                for i in s:
                    # Check if 'i' is an alphanumeric character and is not a comma or period
                    if i.isalnum() == True and i not in [",", "."]:
                        # Append the lowercase version of 'i' to 'str1'
                        str1 += i.lower()
                # Check if 'str1' is equal to its reverse
                if str1 == str1[::-1]:
                    # If 'str1' is a palindrome, return True
                    return True
        except UnicodeDecodeError:
            # If a UnicodeDecodeError occurs (non-ASCII characters in 's'), do nothing and pass
            pass