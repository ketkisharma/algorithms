class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        num_houses = len(nums)
        
        if num_houses == 1 or num_houses == 2:
            return max(nums)
        
        money = []
        money.append(nums[0])
        money.append(nums[1])
        
        for i in range(2, num_houses):
            max_for_current = max(money[:i-1]) + nums[i]
            money.append(max_for_current)
            
        return max(money)
        

"""
Runtime: 28 ms, faster than 81.68% of Python3 online submissions for House Robber.
Memory Usage: 14 MB, less than 15.94% of Python3 online submissions for House Robber.
"""