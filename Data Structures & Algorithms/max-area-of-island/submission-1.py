class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        
        def dfs(row, col):
            outOfBounds = row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])

            if outOfBounds or grid[row][col] == 0 or (row, col) in visited:
                return 0

            visited.add((row, col))

            area = 1

            area += dfs(row + 1, col)
            area += dfs(row - 1, col)
            area += dfs(row, col + 1)
            area += dfs(row, col - 1)

            return area


        def findMaxArea(grid):
            maxArea = 0

            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1 and (row, col) not in visited:
                        area = dfs(row, col)
                        maxArea = max(maxArea, area)

            return maxArea

        return findMaxArea(grid)
