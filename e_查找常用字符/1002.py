class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        min_length_char = min(A, key=len)
        for char in min_length_char:
            if all(char in item  for item in A):
                res.append(char)
                A = [i.replace(char,'',1)  for i in A]

        return res