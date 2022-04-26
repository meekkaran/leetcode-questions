class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Go through every item in the board, and for each item,check whether it resides in the row, the column or the sub-board
        # To check whether a number is in the (3*3) grid, divide each row and each collumn in it by 3. r//3 and c//3
        #we will use a Hashmap as it maps keys to its value pairs.
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set) 
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                # if each value in row/collumn/squares in already in the set, return false else add the number to the set
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3),(c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c] .add(board[r][c])
                squares[(r//3),(c//3)].add(board[r][c])
        return True
        

            
        
        
