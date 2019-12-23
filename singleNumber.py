def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]] += 1
            else:
                d[nums[i]] = 1

        for num, freq in d.items():
            if freq == 1:
                return num