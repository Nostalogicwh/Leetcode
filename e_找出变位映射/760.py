class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        num = []
        for i in A:
            for j in range(len(B)):
                if i == B[j]:
                    num.append(j)
                    break
        return num