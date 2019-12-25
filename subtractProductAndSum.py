def subtractProductAndSum(self, n: int) -> int:
        digitsArr, result = [int(i) for i in str(n)], 1
        for i in digitsArr:
            result*=i
        return result - sum(digitsArr)