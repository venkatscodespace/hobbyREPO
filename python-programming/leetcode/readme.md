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


### Problem #43: Multiply Strings (Difficulty: Medium)

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

**Note:** You must not use any built-in BigInteger library or convert the inputs to integers directly.

### Example 1:
- **Input:** `num1 = "2"`, `num2 = "3"`
- **Output:** `"6"`

### Example 2:
- **Input:** `num1 = "123"`, `num2 = "456"`
- **Output:** `"56088"`

### Constraints:
- `1 <= num1.length, num2.length <= 200`
- `num1` and `num2` consist of digits only.
- Both `num1` and `num2` do not contain any leading zeros, except the number `0` itself.

### Solution

```python
class Solution(object):
    def multiply(self, num1, num2):
        try:
            if ((len(num1) in range(1,201)) and (len(num2) in range(1,201))):
                return str(int(num1) * int(num2))
        except ValueError:
            pass
```

This code defines a `Solution` class with a `multiply` method that multiplies two large numbers represented as strings. The method:
- Checks that the lengths of `num1` and `num2` are within the range of 1 to 200.
- Converts the input strings to integers, performs the multiplication, and returns the result as a string.
- Includes exception handling to manage potential `ValueError` exceptions during string to integer conversion.

### Problem #58: Length of Last Word (Difficulty: Easy)

Given a string `s` consisting of words and spaces, this program calculates the length of the last word in the string. A word is defined as a maximal substring consisting of non-space characters only.

## Example

## Example 1:
Input: "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

## Example 2:
Input: "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

## Example 3:
Input: "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

## Implementation in Python

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        Calculates the length of the last word in a string.

        Args:
        - s: Input string consisting of words and spaces

        Returns:
        - Integer: Length of the last word
        """
        # Split the string into a list of words
        list_s = s.split()

        # Return the length of the last word, which is the last element in the list
        return len(list_s[-1])

# Example usage:
# Initialize Solution object
solution = Solution()

# Example 1:
print(solution.lengthOfLastWord("Hello World"))  # Output: 5

# Example 2:
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4

# Example 3:
print(solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6
