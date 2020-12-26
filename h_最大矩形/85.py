class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        datas = [0]*len(matrix[0])
        maxS = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]=='0'):
                    datas[j]=0
                else:
                    datas[j]+=1
            sample = list(set(datas))
            for idx1 in range(len(sample)):
                mlen,curlen = 0,0
                for idx2 in range(len(matrix[0])):
                    if datas[idx2] >= sample[idx1]:
                        curlen+=1
                    else:
                        maxS = max(maxS, curlen*sample[idx1])
                        curlen=0
                    mlen=max(mlen,curlen)
                maxS = max(maxS, mlen*sample[idx1])
        return maxS