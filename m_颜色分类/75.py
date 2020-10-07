class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        i0 = 0
        i2 = len(nums) - 1

        while i <= i2:
            if nums[i] == 0:
                nums[i0], nums[i] = nums[i], nums[i0]
                i0 += 1
                i += 1  # 因为i是从前往后的，所以前面的数已经查过了，找到0移动到前面就可以往下一个数走了。
            elif nums[i] == 2:
                nums[i2], nums[i] = nums[i], nums[i2]
                i2 -= 1  # 因为i是从前往后的，所以后面的数还没查过，找到2移动到后面，还要停一下。
            else:
                i += 1