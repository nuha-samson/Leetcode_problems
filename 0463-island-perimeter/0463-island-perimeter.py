class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        x = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    x += 4
                    if i + 1 < rows and grid[i + 1][j] == 1:
                        x -= 2
                    if j + 1 < cols and grid[i][j + 1] == 1:
                        x -= 2
        return x