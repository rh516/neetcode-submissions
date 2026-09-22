from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def isInBounds(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])

        visited = set()
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))

        currentLevel = 1

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for deltaRow, deltaCol in directions:
                    neighborRow = row + deltaRow
                    neighborCol = col + deltaCol

                    if (
                        isInBounds(neighborRow, neighborCol) and 
                        (neighborRow, neighborCol) not in visited and
                         grid[neighborRow][neighborCol] == 2147483647
                    ):
                        visited.add((neighborRow, neighborCol))
                        grid[neighborRow][neighborCol] = currentLevel
                        queue.append((neighborRow, neighborCol))

            currentLevel += 1




