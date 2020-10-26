class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l = len(nums)
        arr = [0]*l
        for i in range(l):
            sum = 0
            for j in range(l):
                if nums[i] > nums[j]:
                    sum += 1
            arr[i] = sum
        return arr