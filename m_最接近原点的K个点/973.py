class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        l = len(points)
        dic = {}
        for i in range(l):
            x = abs(points[i][0])
            y = abs(points[i][1])
            j = (x*x + y*y) ** 0.5
            a = {i:j}
            dic.update(a)
        dic = sorted(dic,key=dic.__getitem__)
        ans = []
        for i in range(K):
            ans.append(points[dic[i]])
        return ans