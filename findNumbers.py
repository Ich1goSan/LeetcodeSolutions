def findNumbers(self, nums: List[int]) -> int:
        resArr = [i for i in nums if len(str(i))%2==0]
        return len(resArr)