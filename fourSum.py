def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    s = set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            m = {}
            for k in range(j+1, len(nums)):
                x = target - nums[i] - nums[j] - nums[k]
                if x not in m:
                    m[nums[k]] = k
                else:
                    s.add((x, nums[i], nums[j], nums[k]))
    return list(s)
    
