#https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        temp_results = {}

        for i in nums: 
            if i in temp_results:
                temp_results[i] += 1
            else: 
                temp_results[i] = 1

        sorted_result = self.MergeSort([x for x in temp_results.items()])
        return [sorted_result[x][0] for x in range(len(sorted_result)) if x < k]
    
    def MergeSort(self, input):
        if len(input) <= 1:
            return input 
        left = []
        right = []

        for i in range(len(input)):
            if i < (len(input)/2):
                left.append(input[i])
            else:
                right.append(input[i])
        left = self.MergeSort(left)

        right = self.MergeSort(right)

        return self.Merge(left, right)
    
    def Merge(self, left, right):
        result = []
        while(len(left) != 0 and len(right) != 0):
            if left[0][1] >= right[0][1]: 
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:] 
        while(len(left) != 0):
            result.append(left[0])
            left = left[1:]

        while(len(right) != 0):
            result.append(right[0])
            right = right[1:]
        return result
            





input = [2, 2, 2, 1, 1, 6, 5, 4, 3, 2, 1, 2, 4, 2]

run = Solution()
print(run.topKFrequent(input, 5))