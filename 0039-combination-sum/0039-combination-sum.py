class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans, sol = [], []
        
        def backtrack(i, cur_sum):
            if cur_sum == target:
                ans.append(sol[:])
                return
            
            if cur_sum > target or i == n:
                return
            
            backtrack(i+1, cur_sum)
            
            sol.append(candidates[i])
            backtrack(i, cur_sum + candidates[i])
            sol.pop()
            
        backtrack(0, 0)
        return ans
    
    # TC: O(n**t)
    # SC: O(n)
            