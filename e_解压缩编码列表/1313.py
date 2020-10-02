class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            if i % 2 == 0:
                continue
            else:
                for j in range(nums[i-1]):
                    arr.append(nums[i])
        return arr