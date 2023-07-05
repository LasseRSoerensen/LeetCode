class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        start = False
        for i in range(len(s)):

            if s[len(s) - (i + 1)] != " ":
                if start == False:
                    start = True 
                counter += 1
            elif s[len(s) - (i + 1)] == " ":
                if start == False:
                    continue
                else: 
                    break 
        return counter





test = Solution()

print(test.lengthOfLastWord("dg sf wadwa as dfhejsa"))