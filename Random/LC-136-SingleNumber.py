#https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = {}

        for i in nums: 
            if i in answer: 
                answer[i] += 1 
            else: 
                answer[i] = 1 
        

        for i in answer:
            if answer[i] == 1:
                return i