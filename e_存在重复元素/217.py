class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
         if len(nums) == len(set(nums)):#用set去重，判断数组长度是否一致
             return False
         else:
             return True