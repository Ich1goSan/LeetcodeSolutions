def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x not in m:
                m[nums[i]] = i
            else:
                return [m[x], i]