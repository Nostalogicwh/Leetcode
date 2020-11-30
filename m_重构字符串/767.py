class Solution:
    def reorganizeString(self, S: str) -> str:
        res = ""
        counter = collections.Counter(S)
        # 边界条件
        if max(counter.values()) > (len(S)+1) // 2:
            return res
        
        # 将字母添加到堆中
        pq = []
        for key,val in counter.items():
            heapq.heappush(pq,(-val,key))
            
        prev = (0,None)
        
        # 开始重构字符串
        while pq:
            v,k = heapq.heappop(pq)
            res += k
            if prev[0] < 0:
                heapq.heappush(pq,prev)
            prev = (v+1,k)

        return res