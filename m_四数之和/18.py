class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        l = len(nums)
        arr = [0]*4
        suma = []
        ans = []
        for i in range(l):
            if i+1 <= l-1:
                if (nums[i] + 3*nums[i+1]) > target:
                    break
            if (nums[i] + 3*nums[-1]) < target:
                continue            
            for j in range(i+1,l):
                if j+1 <= l-i-1:
                    if (nums[j] + 2*nums[j+1]) > (target-nums[i]):
                        break
                if (nums[j] + 2*nums[-1]) < (target-nums[i]):
                    continue
                for n in range(j+1,l):
                    if n+1 <= l-i-j-1:
                        if (nums[n] + nums[n+1]) > (target-nums[i]-nums[j]):
                            break
                    if (nums[n] + nums[-1]) < (target-nums[i]-nums[j]):
                        continue
                    for m in range(n+1,l):
                        if nums[i]+nums[j]+nums[n]+nums[m] == target:
                            arr = [nums[i],nums[j],nums[n],nums[m]]
                            suma.append(arr)
        for i in range(len(suma)):
            if suma[i] in ans:
                continue
            else:
                ans.append(suma[i])
        return ans