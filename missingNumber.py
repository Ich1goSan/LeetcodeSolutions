def missingNumber(self, nums: List[int]) -> int:
        return int(len(nums)/2*(len(nums)+1) - sum(nums))