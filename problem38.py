# This problem was asked by Microsoft.
# You have an N by N board. Write a function that, 
# given N, returns the number of    possible arrangements 
# of the board where N queens can be placed on the board 
# without threatening each other, i.e. no two queens share 
# the same row, column, or diagonal.

#Saw it from 
#https://github.com/vineetjohn/daily-coding-problem/blob/master/solutions/problem_038.py
def is_safe_position(board, row):
    #checking if there is a queen on same line here
    if row in board:
        return False

    col = len(board)

    #checking diagonals here
    for occupied_col, occupied_row in enumerate(board):
        if abs(occupied_row-row) == abs(occupied_col - col):
            return False

    return True

def queen_configurations(board, n):
    if n == len(board):
        return 1
    
    count = 0

    for row in range(n):
        if is_safe_position(board, row):
            count += queen_configurations(board + [row], n)

    return count
    



if __name__ == "__main__":
    assert not is_safe_position([0, 2], 0)
    assert not is_safe_position([0, 2], 2)
    assert is_safe_position([0, 8], 3)
    assert not is_safe_position([1, 3], 2)
    assert is_safe_position([], 1)

    assert queen_configurations([], 2) == 0
    assert queen_configurations([], 4) == 2
    assert queen_configurations([], 5) == 10
    assert queen_configurations([], 8) == 92

    print('All tests pass!')