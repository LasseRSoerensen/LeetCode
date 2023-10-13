class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        min1, max1 = 0, len(matrix) - 1

        while min1 <= max1:
            average1 =  int(min1 + (max1 - min1) / 2)
            if target >= matrix[average1][0] and target <= matrix[average1][len(matrix[average1]) - 1]:
                min2, max2 = 0, len(matrix[average1]) - 1
                while min2 <= max2: 
                    average2 =  int(min2 + (max2 - min2) / 2)
                    if matrix[average1][average2] == target or matrix[average1][min2] == target or matrix[average1][max2] == target:
                        return True
                    elif target > matrix[average1][average2]:
                        min2 = average2 + 1
                    elif target < matrix[average1][average2]:
                        max2 = average2 - 1
                return False 
            elif target < matrix[average1][0]:
                max1 = average1 - 1
            elif target > matrix[average1][len(matrix[average1]) - 1]:
                min1 = average1 + 1
                