class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        if int(S) == 0 and len(S) > 1:
            return [0]*len(S)
        def match(m,n,S):
            feibo = []
            feibo.append(int(S[:m]))
            feibo.append(int(S[m:m+n]))
            k = m + n 
            k2 = len(str(feibo[-1] + feibo[-2]))
            while(k + k2 <= len(S)):
                k1 = feibo[-1] + feibo[-2]
                k2 = len(str(k1))
                if int(S[k:k+k2]) == k1:
                    feibo.append(k1)
                    k += k2
                else:
                    return False,feibo
            str1 = ''
            for i in feibo:
                str1 += str(i)
            if str1 != S or len(feibo) < 3:
                return False,feibo
            else:
                return True,feibo

        for i in range(1,int(len(S) / 2 + 1)):
            for j in range(1,int(len(S) / 2 + 1)):
                if match(i,j,S)[0] == True:
                    if match(i,j,S)[1][-1] > 2**31 - 1:
                        return []
                    else:
                        return match(i,j,S)[1]
                else:
                    continue
        return []