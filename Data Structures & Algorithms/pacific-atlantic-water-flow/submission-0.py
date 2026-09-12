class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        for every cell run a dfs to try to reach both oceans

        '''
        pacific = set()
        atlantic = set()
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        soln = []

        def inBounds(row, col):
            return row >= 0 and col >= 0 and row < len(heights) and col < len(heights[0])

        def dfs(row, col, visited):
            visited.add((row, col))
            currentHeight = heights[row][col]

            for direction in directions:
                deltaRow, deltaCol = direction
                newRow = row + deltaRow
                newCol = col + deltaCol

                if not inBounds(newRow, newCol):
                    continue
                if (newRow, newCol) in visited:
                    continue
                if currentHeight > heights[newRow][newCol]:
                    continue

                dfs(newRow, newCol, visited)

        for row in range(len(heights)):
            dfs(row, 0, pacific)
            dfs(row, len(heights[0]) - 1, atlantic)

        for col in range(len(heights[0])):
            dfs(0, col, pacific)
            dfs(len(heights) - 1, col, atlantic)


        for cell in pacific:
            if cell in atlantic:
                soln.append(cell)

        return soln
        
