class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        min_idx = l
        
        if min_idx == 0:
            l, r = 0, n-1
        elif target >= nums[0] and target <= nums[min_idx-1]:
            l, r = 0, min_idx-1
        else:
            l, r = min_idx, n-1
            
        while l <= r:
            m = (l+r)//2
            
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1
    
    # TC: O(log n)
    # SC: O(1)
        