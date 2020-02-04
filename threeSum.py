def threeSum(nums):
    s = set()
    nums.sort()
    for i in range(len(nums)):
        m = {}
        for j in range(i+1, len(nums)):
            x = -nums[i] - nums[j]
            if x not in m:
                m[nums[j]] = j
            else:
                s.add((x,nums[i],nums[j]))
    return list(s)