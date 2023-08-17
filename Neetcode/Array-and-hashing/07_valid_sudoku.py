"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for column in range(9):

                if board[row][column] == ".":
                    continue
                elif (
                    board[row][column] in rows[row] or
                    board[row][column] in columns[column] or
                    board[row][column] in squares[(row//3,column//3)]
                ):
                    return False
                else:
                    rows[row].add(board[row][column])
                    columns[column].add(board[row][column])
                    squares[(row//3,column//3)].add(board[row][column])
        
        return True