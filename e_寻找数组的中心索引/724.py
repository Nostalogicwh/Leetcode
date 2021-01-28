class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        a = sum(nums)
        b = 0
        for i in range(len(nums)):
            if b*2 == a - nums[i]:
                return i
            b += nums[i]
        return -1