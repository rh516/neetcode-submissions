from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def inBounds(row, col):
            return row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0])



        queue = deque()
        fresh = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                val = grid[row][col]
                if val == 2:
                    queue.append((row, col))
                elif val == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue and fresh > 0:
            rottenFruitsThisMinute = len(queue)

            for _ in range(rottenFruitsThisMinute):
                row, col = queue.popleft()

                for direction in directions:
                    x, y = direction

                    newRow = row + x
                    newCol = col + y

                    if inBounds(newRow, newCol) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        fresh -= 1

            minutes += 1

        if fresh > 0:
            return -1

        return minutes