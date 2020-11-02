class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = len(arr)
        ans = 0
        for i in range(l-2):
            for j in range(i+1,l-1):
                for k in range(j+1,l):
                    if abs(arr[i]-arr[j])<=a:
                        if abs(arr[j]-arr[k])<=b:
                            if abs(arr[i]-arr[k])<=c:
                                ans += 1
        return ans