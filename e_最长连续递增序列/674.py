class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        temp = 1
        ans = 1
        if len(nums) < 2:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                temp += 1
            else:
                ans = max(ans,temp)
                temp = 1
        ans = max(ans,temp)
        return ans
