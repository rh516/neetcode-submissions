class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}

        for prereq in prerequisites:
            courseB, courseA = prereq

            if courseA not in adjList:
                adjList[courseA] = [courseB]
            else:
                adjList[courseA].append(courseB)

        visiting = set()
        visited = set()

        def dfs(course):
            if course in visiting:
                return False
            if course in visited:
                return True

            visiting.add(course)

            if course in adjList:
                for neighbor in adjList[course]:
                    if not dfs(neighbor):
                        return False

            visiting.remove(course)
            visited.add(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False

        return True

