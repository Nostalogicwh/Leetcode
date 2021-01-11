class Solution:
    def dfs(self,res,graph,visited,x):
        for neighbor in graph[x]:
            if not visited[neighbor]:
                visited[neighbor] = 1
                res.append(neighbor)
                self.dfs(res,graph,visited,neighbor)
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 建图
        graph = [[] for _ in range(len(s))]
        visited = [0] * len(s)
        for x,y in pairs:
            graph[x].append(y)
            graph[y].append(x)
        
        res = list(s)
        for i in range(len(s)):
            if not visited[i]:
                # 获取连通节点
                connected_nodes = []
                self.dfs(connected_nodes,graph,visited,i)
                # 重新赋值
                indices = sorted(connected_nodes)
                string = sorted(res[node] for node in connected_nodes)
                for j,ch in zip(indices,string):
                    res[j] = ch
            
        return "".join(res)