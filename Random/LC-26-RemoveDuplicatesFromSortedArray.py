#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unik = {}
        modified_counter = 0

        for i in range(len(nums)): 
            i -= modified_counter
            if nums[i] not in unik: 
                unik[nums[i]] = i
            else:
                nums.pop(i)
                modified_counter += 1
                
        return len(unik)

test = Solution()

print(test.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))