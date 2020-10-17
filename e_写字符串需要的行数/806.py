class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        dictnum = dict(zip("abcdefghijklmnopqrstuvwxyz",widths))
        row = 0
        num = 0
        for i in S:
            summ = dictnum[i]
            num += summ
            if num > 100:
                row += 1
                num = summ

        return row+1,num