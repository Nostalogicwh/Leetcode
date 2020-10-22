class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        
        max_index = {item: idx for idx, item in enumerate(S)}
        print(max_index)
        start, end = 0, 0
        ans = []
        
        for idx, i in enumerate(S):
            end = max(end, max_index[i])
            if idx == end:
                ans.append(end - start + 1)
                start = idx + 1
        
        return ans