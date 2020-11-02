class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in nums1:
            if i in nums2:
                if i in arr:
                    continue
                else:
                    arr.append(i)
        return arr