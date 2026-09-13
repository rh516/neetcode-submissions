class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
            backtracking
            sort candidates
            keep track of current path and sum of that current path
            return condition: current sum == target
            if currentSum + candidate > target, break out of loop
            add candidate one at a time, skip over if duplicate
            recurse with updated path and sum


            []
        '''
        soln = []
        path = []
        candidates.sort()

        def backtrack(startIndex, currentSum):
            if currentSum == target:
                soln.append(path[:])

            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i - 1]:
                    continue
                
                if currentSum + candidates[i] > target:
                    break

                path.append(candidates[i])
                backtrack(i + 1, currentSum + candidates[i])
                path.pop()

        backtrack(0, 0)
        return soln