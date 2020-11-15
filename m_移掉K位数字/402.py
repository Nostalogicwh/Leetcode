class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num_length = len(num)
        if num_length <= k:
            return "0"
        
        left_count = num_length - k
        res = ""
        count = 0
        begin = 0
        
        while count < left_count:
            min_index = 0
            min_num = float('inf')
            for i in range(begin, k + count + 1):
                # 找到最小数
                if int(num[i]) < min_num:
                    min_index = i
                    min_num = int(num[i])
            # 把找到的最小数加入结果列表
            res += str(min_num)
            # 设置下一轮查找范围的起点
            begin = min_index + 1
            count += 1
            
        return "0" if len(res) == 0 else str(int(res))