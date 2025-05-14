
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, columns = [0] * n, [0] * n
        d1, d2 = 0, 0
        player = 1  # A = 1, B = -1

        for r, c in moves:
            rows[r] += player
            columns[c] += player
            if r == c:
                d1 += player
            if r + c == n - 1:
                d2 += player
            # Corrected variable name: columns instead of cols
            if abs(rows[r]) == n or abs(columns[c]) == n or abs(d1) == n or abs(d2) == n:
                return "A" if player == 1 else "B"
            player *= -1

        return "Draw" if len(moves) == n * n else "Pending"
