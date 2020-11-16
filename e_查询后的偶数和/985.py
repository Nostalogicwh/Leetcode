class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        even = sum([i for i in A if i%2==0])
        res = []
        for v,i in queries:
            A[i] += v
            if A[i] % 2 == 0:
                if v%2==0:
                    res.append(even+v)
                    even += v
                else:
                    res.append(even+A[i])
                    even += A[i]
            else:
                if v%2==0:
                    res.append(even)
                else:
                    res.append(even+v-A[i])
                    even -= A[i] - v
        return res