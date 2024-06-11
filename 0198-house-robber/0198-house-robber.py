class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        
        prev = nums[0]
        curr = max(nums[0], nums[1])
        
        for i in range(2,n):
            prev , curr = curr , max(nums[i] + prev, curr)
        
        return curr
    
    # TC: O(n)
    # SC: O(1)