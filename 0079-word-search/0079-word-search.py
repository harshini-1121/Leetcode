#can use the array sorting or matrox for this and checking letter by letter using string to know the next is a adjacent cells or not if one letter is not adjacent f other i will return as false.
#using the DS concept of graph for search the neighbour  in this.May be DFS where backtracking will be easier

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board), len(board[0])
        def dfs(r,c,index):
            if index == len(word):
                return True    
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] !=word[index]:
                return False
            
            temp = board[r][c]
            board[r][c] = '#'
            
            result = (dfs(r+1, c, index+1) or
                      dfs(r-1, c, index+1) or
                      dfs(r, c+1, index+1) or
                      dfs(r, c-1, index+1))
            board[r][c] = temp

            return result
        for i in range(rows):
            for j in range (cols):
                if board [i][j] == word[0] and dfs(i,j,0):
                    return True

        return False                
