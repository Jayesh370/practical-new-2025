print("Enter the number of queens: ")
N = int(input())
def solveNQueens(n: int):
    # Step 1: Initialize sets to keep track of constraints
    col = set()        # columns where queen already placed
    posDiag = set()    # positive diagonals (r + c)
    negDiag = set()    # negative diagonals (r - c)

    res = []   # List to store all the solutions

    # Step 2: Create a blank chessboard
    board = [['.' for _ in range(n)] for _ in range(n)]  # n x n board with '.'

    # Step 3: Define a function for backtracking
    def backtrack(r):
        # Base Case: If we reach row n, we found a solution
        if (r == n):
            res.append([''.join(row) for row in board])
            return

        # Step 4: Try placing queen in every column in current row
        for c in range(n):
            # Step 5: Check if placing at (r,c) is safe
            if (c in col or (r + c) in posDiag or (r - c) in negDiag):
                continue  # Not safe, skip this column

            # Step 6: Place queen
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = 'Q'

            # Step 7: Move to next row
            backtrack(r + 1)

            # Step 8: Backtrack (remove queen and try next possibility)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = '.'

    # Step 9: Start from row 0
    backtrack(0)
    return res

# Step 10: Function to print solutions
def printSolutions(boards):
    for board in enumerate(boards):
        print(f"Solution: {board[0]+1}")
        for row in board[1]:
            for col in row:
                print(col, end=' ')
            print()
        print()

# Step 11: Main driver code
if __name__ == "__main__":
    boards = solveNQueens(N)  # Example for 8x8 board
    printSolutions(boards)
