class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        add, i, count = 1, 0, 0
        while add <= n:
            if i < len(nums) and nums[i] <= add:
                add += nums[i] # from [1, add] to [1, add + nums[i]]
                i += 1
            else:
                add += add # from [1, add] to [1, 2add]
                count += 1
        return count