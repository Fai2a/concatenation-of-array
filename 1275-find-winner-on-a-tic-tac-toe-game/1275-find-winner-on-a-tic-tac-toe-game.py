from typing import List

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # Grid size
        n = 3
        # Create a board with empty strings
        board = [[''] * n for _ in range(n)]

        # Players turn: even index → A, odd index → B
        for i, (r, c) in enumerate(moves):
            board[r][c] = 'X' if i % 2 == 0 else 'O'

        # Function to check if someone has won
        def check_winner(symbol):
            # Check rows, columns, and diagonals
            for i in range(n):
                if all(board[i][j] == symbol for j in range(n)): return True
                if all(board[j][i] == symbol for j in range(n)): return True
            if all(board[i][i] == symbol for i in range(n)): return True
            if all(board[i][n - 1 - i] == symbol for i in range(n)): return True
            return False

        # Check for winner
        if check_winner('X'):
            return "A"
        elif check_winner('O'):
            return "B"
        elif len(moves) == n * n:
            return "Draw"
        else:
            return "Pending"
