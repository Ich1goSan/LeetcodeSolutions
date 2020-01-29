def majorityElement(self, nums):
    c = len(nums) // 2
    m = {}
    for i in nums:
        if i not in m:
            m[i] = 1
        else:
            m[i] += 1

    return max(m, key=m.get)
