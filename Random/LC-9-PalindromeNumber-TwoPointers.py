#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringNumber = str(x)

        for i in range(len(stringNumber)):
            if stringNumber[i] == stringNumber[len(stringNumber) - (1 + i)]:
                continue
            else: 
                return False
        return True



test = Solution()
print(test.isPalindrome(4114))
