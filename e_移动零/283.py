class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1 = len(nums)
        while True:
            try:
                nums.remove(0)
            except:
                break
        l2 = len(nums)
        for i in range(l1-l2):
            nums.append(0)