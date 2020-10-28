class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash = []
        ans = []
        for i in arr:
            if i in hash:
                pass
            else:
                hash.append(i)
                ans.append(arr.count(i))
        for i in ans:
            if ans.count(i) > 1:
                return False
        return True