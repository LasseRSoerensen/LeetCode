class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:

            if len(stack) >= 1:

                if i == "}" and stack[len(stack) - 1] == "{":
                    stack.pop()
                elif i == ")" and stack[len(stack) - 1] == "(":
                    stack.pop()
                elif i == "]" and stack[len(stack) - 1] == "[":
                    stack.pop()        
                else: 
                    stack.append(i)

            else:
                stack.append(i)
        if len(stack) == 0:
            return True
        else: 
            return False       



run = Solution()


print(run.isValid("()"))