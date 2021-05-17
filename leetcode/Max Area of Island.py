class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        dr = [-1,0,1,0]
        dc = [0,1,0,-1]
        
        visit = [[0]* m for _ in range(n) ]
        
        self.cnt = 0 
        def dfs ( r , c ) :
            visit[r][c] = 1 
            for i in range(4):
                nr, nc = dr[i] + r , dc[i]+ c
                if 0<= nr < n and 0<= nc < m :                    
                    if grid[nr][nc] == 1 and visit[nr][nc] != 1 :
                        self.cnt  += 1
                        dfs(nr,nc)
                        
        ans = 0
        for i in range(n):
            for j in range(m):
                if visit[i][j] == 0 and grid[i][j] == 1:
                    self.cnt  = 1
                    dfs(i,j)
                    print(i,j,self.cnt)
                    ans  = max(self.cnt , ans)
                    
            
        return ans 
