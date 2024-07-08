## Introduction to LeetCode Problems by venkatscodespace

### Problem #125: Valid Palindrome (Difficulty: Medium)
#### Companies: Facebook, Microsoft, and Amazon​
A phrase is considered a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Examples

#### Example 1:
**Input:** `s = "A man, a plan, a canal: Panama"`  
**Output:** `true`  
**Explanation:** `"amanaplanacanalpanama"` is a palindrome.

#### Example 2:
**Input:** `s = "race a car"`  
**Output:** `false`  
**Explanation:** `"raceacar"` is not a palindrome.

#### Example 3:
**Input:** `s = " "`  
**Output:** `true`  
**Explanation:** `s` is an empty string `""` after removing non-alphanumeric characters. Since an empty string reads the same forward and backward, it is a palindrome.

### Constraints:
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

### Solution Code

Here is the solution code with detailed comments explaining each line:

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        try:
            # Attempt to decode the string 's' to ASCII to ensure it contains only valid ASCII characters
            s.encode('ascii')
            
            # Check if the length of 's' is between 1 and 200,000 inclusive
            if (len(s) >= 1) and (len(s) <= 2 * (10 ** 5)):
                # Initialize an empty string 'str1' to store alphanumeric characters from 's'
                str1 = ""
                
                # Iterate through each character 'i' in the string 's'
                for i in s:
                    # Check if 'i' is an alphanumeric character
                    if i.isalnum():
                        # Append the lowercase version of 'i' to 'str1'
                        str1 += i.lower()
                
                # Check if 'str1' is equal to its reverse
                return str1 == str1[::-1]
                
        except UnicodeDecodeError:
            # If a UnicodeDecodeError occurs (non-ASCII characters in 's'), return False
            return False

# Examples to test the code
solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))  # Output: true
print(solution.isPalindrome("race a car"))  # Output: false
print(solution.isPalindrome(" "))  # Output: true
```

This code defines a `Solution` class with an `isPalindrome` method that checks if the given string `s` is a palindrome according to the problem's definition. The method processes the string to remove non-alphanumeric characters and convert all letters to lowercase before checking if it reads the same forward and backward.
