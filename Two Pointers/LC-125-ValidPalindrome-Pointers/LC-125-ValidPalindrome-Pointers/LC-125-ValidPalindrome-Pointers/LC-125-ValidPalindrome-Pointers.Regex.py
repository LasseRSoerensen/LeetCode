#https://leetcode.com/problems/valid-palindrome/
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #find all valid instances through regular expression
        valid_string = re.findall("([a-z]|[0-9])", s.lower())
        #go through the string by comparing the first element, with the last, moving closer to the middle each iteration
        for i in range(len(valid_string)): 
            if valid_string[i] == valid_string[len(valid_string) - (i + 1)]:
                continue
            else: 
                return False
        return True





test = Solution()


print(test.isPalindrome("race a car"))