class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emp=0
        drk=0

        while emp>=numExchange or numBottles>0: #空瓶还能换 或 还有酒没喝 
            drk+=numBottles # 喝掉
            emp+=numBottles # 空瓶加起来
            numBottles=emp//numExchange # 换酒
            emp=emp%numExchange # 剩多少空瓶？
        return drk