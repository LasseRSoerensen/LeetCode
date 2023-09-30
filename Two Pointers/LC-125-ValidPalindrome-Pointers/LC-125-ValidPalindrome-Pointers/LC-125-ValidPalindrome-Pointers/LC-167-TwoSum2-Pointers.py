class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start = 0
        end = len(numbers) - 1

        while(True): 
            if numbers[start] + numbers[end] == target: 
                return [start + 1, end + 1]
            elif numbers[start + 1] + numbers[end] <= target: 
                start += 1
            else: 
                end += -1
