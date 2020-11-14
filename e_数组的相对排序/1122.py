class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr3 = []
        arr4 = []
        for i in arr2:
            for j in arr1:
                if j == i:
                    arr3.append(j)
        for i in arr1:
            if i in arr3:
                pass
            else:
                arr4.append(i)
        arr4 = sorted(arr4)
        for i in arr4:
            arr3.append(i)
        return arr3