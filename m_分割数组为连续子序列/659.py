class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # 记录元素出现次数
        counter = dict()
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            
        end = dict()
        for n in nums:
            if counter[n] == 0:
                continue
                
            counter[n] -= 1
            if end.get(n - 1, 0) > 0:
                # 添加到已有子序列的末尾
                end[n - 1] -= 1
                end[n] = end.get(n, 0) + 1
            elif counter.get(n + 1, 0) > 0 and counter.get(n + 2, 0) > 0:
                # 添加到子序列头部
                counter[n + 1] -= 1
                counter[n + 2] -= 1
                end[n + 2] = end.get(n + 2, 0) + 1
            else:
                return False
        return True