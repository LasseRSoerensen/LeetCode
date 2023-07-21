#https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = len(nums) / 2
        uniqueElements = {}

        for i in range(len(nums)): 
            if nums[i] in uniqueElements:
                uniqueElements[nums[i]] += 1
            else: 
                uniqueElements[nums[i]] = 1
        
        for i in uniqueElements:
            if uniqueElements[i] >= majority:
                return i






test = Solution()


print(test.majorityElement([2, 2, 1, 1, 1, 2, 2, 3, 2]))