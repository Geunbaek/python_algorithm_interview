from collections import deque

class Solution:
    # solve 1
    def numIslands(self, grid: list[list[str]]) -> int:
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        cnt =0
        def bfs(x, y):
            q = deque()
            q.append((x, y))
            grid[y][x] = '0'
            while q:
                now_x, now_y = q.popleft()
                for i in range(4):
                    nx = now_x + dx[i]
                    ny = now_y + dy[i]
                    if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                        if grid[ny][nx] == '1':
                            grid[ny][nx] = '0'
                            q.append((nx, ny))
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    bfs(x, y)
                    cnt += 1

        return cnt
    # solve 2
    def numIslands_2(self, grid: list[list[str]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid) or grid[y][x] == '0':
                return

            grid[y][x] = "0"
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x+1, y)
            dfs(x, y+1)
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    dfs(x, y)
                    count += 1
        return count

solution = Solution()
print(solution.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""