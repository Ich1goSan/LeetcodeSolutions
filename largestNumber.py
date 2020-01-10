def largestNumber(self, nums: List[int]) -> str:
    if all(item == 0 for item in nums):
        return "0"
     return ''.join(sorted([str(i) for i in nums], key=cmp_to_key(lambda x, y: 1 if x + y < y + x else -1)))