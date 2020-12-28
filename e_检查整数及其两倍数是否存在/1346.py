class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in arr:
            if i == 0:
                if arr.count(i) > 1:
                    return True
            elif 2*i in arr:
                return True
        return False