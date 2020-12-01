class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = -1
        b = -1
        l = len(nums)
        for i in range(l):
            if nums[i] == target:
                a = i
                break
        for i in range(l-1,-1,-1):
            if nums[i] == target:
                b = i
                break
        return [a,b]