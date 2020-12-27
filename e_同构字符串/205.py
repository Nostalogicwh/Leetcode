class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict={}
        for i in range(len(s)):
            if s[i] in dict:    #判断该元素是否之前出现过
                if dict[s[i]]!=t[i]:    #如果之前出现过，现在对应的值却不一样，返回False
                    return False
            else:
                if t[i] in dict.values():   #判断该元素是否在字典的值里面，如果在里面就说明对应的值不一样
                    return False
                dict[s[i]]=t[i] #将两个值录入字典中(记录下s[i]所变换后的字母)
        return True