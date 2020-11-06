from collections import defaultdict as d

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = d(list)

        for i in arr:
            c = 0
            for s in str(bin(i)):
                if s == "1":
                    c += 1
            dic[c].append(i)

        output = []
        for j in range(15):
            if dic[j]:
                for temp in sorted(dic[j]):
                    output.append(temp)

        return output