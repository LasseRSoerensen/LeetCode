
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        #keep track of the column values 
        col = {"0": [], "1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [],} 
        temp_squares = [[], [], []]

        #loop through columns
        for i in range(len(board)):
            temp_row = []

            if i < 3:
                
                pass
            elif i >= 3 and i < 6:
                pass
            else: 
                pass
         


            #loop through rows
            for j in range(len(board[i])):
                #check to see if value is in the row and col else add it
                if board[i][j] in temp_row or board[i][j] in col[str(j)]:
                    return False
                elif board[i][j] != ".": 
                    temp_row.append(board[i][j])
                    col[str(j)].append(board[i][j])


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]




run = Solution()

print(run.isValidSudoku(board))