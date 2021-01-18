class Solution(object):
    def accountsMerge(self, accounts):
        # 用parents维护每一行的父亲节点
        # 如果parents[i] == i, 表示当前节点为根节点
        parents = [i for i in range(len(accounts))]
        dic = {}
        # 查找x的根root
        def find(x):
            root = x 
            while root != parents[root]:
                root = parents[root]
            return root
        # 把x和y合并
        def union(x, y):
            parents[find(x)] = find(y)

        # 如果发现某一行的某个邮箱在之前行出现过，那么把该行的index和之前行合并（union）即可
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email in dic:
                    union(dic[email], i)
                else:
                    dic[email] = i 

        users = collections.defaultdict(set)
        res = []
        # 1. users：表示每个并查集根节点的行有哪些邮箱
        # 2. 使用set：避免重复元素
        # 3. 使用defaultdict(set)：不用对每个没有出现过的根节点在字典里面做初始化
        for i in range(len(accounts)):
            for account in accounts[i][1:]:
                users[find(i)].add(account)

        # 输出结果的时候注意结果需按照字母顺序排序（虽然题目好像没有说）
        for key, val in users.items():
            res.append([accounts[key][0]] + sorted(val))
        
        return res