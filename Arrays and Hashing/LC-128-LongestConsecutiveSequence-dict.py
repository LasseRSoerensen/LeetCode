#https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        print(nums)
        record = []
        log = 0
        for i in range(len(nums)):
            if len(record) == 0 or nums[i] == record[-1] + 1: 
                record.append(nums[i])
            elif nums[i] == record[-1]:
                continue
            else: 
                if len(record) > log:
                    log = len(record)
                record = [nums[i]]
        if log > len(record): 
            return log
        else: 
            return len(record)
            
test = Solution()



print(test.longestConsecutive([1, 2, 0, 1]))