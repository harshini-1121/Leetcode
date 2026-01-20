class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        board = [ ['.' for j in range(n)] for i in range(n) ]
        dig1 = set()
        dig2 = set()
        cols = set()

        def backtrack(r):
            if r==n: # found solution
                solution = []
                for row in board:
                    str_row = "".join(row)
                    solution.append(str_row)
                res.append(solution)
                return 

            for c in range(n):
                if c in cols or (r+c) in dig1 or (r-c) in dig2 :
                    continue

                cols.add(c)
                dig1.add(r+c)
                dig2.add(r-c)
                board[r][c] = "Q"
                backtrack(r+1)
                cols.remove(c)
                dig1.remove(r+c)
                dig2.remove(r-c)
                board[r][c] = "."

        backtrack(0)
        return len(res)