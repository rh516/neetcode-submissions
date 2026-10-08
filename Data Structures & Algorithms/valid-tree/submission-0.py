class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        neighbors = {num: [] for num in range(n)}

        for edge in edges:
            a, b = edge

            neighbors[a].append(b)
            neighbors[b].append(a)

        
        def dfs(node, prevNode):
            if node in visited:
                return False

            visited.add(node)

            for neighbor in neighbors[node]:

                if neighbor == prevNode:
                    continue

                if dfs(neighbor, node) == False:
                    return False

            return True

        if dfs(0, -1) == False:
            return False

        return len(visited) == n

