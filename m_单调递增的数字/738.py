class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        nums = list(str(N))
        length = len(nums)
        begin = 0
        # N 是否符合条件
        is_result = True
        max_num = float('-inf')
        
        # 从前往后观察
        for i in range(1, length):
            num = int(nums[i])
            pre_num = int(nums[i - 1])
            # 记录最大值
            if pre_num > max_num:
                begin = i - 1
                max_num = pre_num
            if pre_num > num:
                is_result = False
                break
        
        # 如果 N 本身符合条件，直接返回 N
        if is_result:
            return N
        
        # begin 位置减去 1，后面全部替换为 9
        nums[begin] = str(int(nums[begin]) - 1)
        for i in range(begin + 1, length):
            nums[i] = '9'
                    
        return int("".join(nums))