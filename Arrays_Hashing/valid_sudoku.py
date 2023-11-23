from typing import List
import collections

def isValidSudoku(board: List[List[str]]) -> bool:
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdicts(set) # key = (row/3, cols/3)

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            if (board[row][col] in rows[row] or 
                board[row][col] in rows[col] or
                board[row][col] in squares[(row // 3, col // 3)]):
                return False
            cols[col].add(board[row][col])
            rows[row].add(board[row][col])
            squares[(row // 3, col // 3)].add(board[row][col])
    return True