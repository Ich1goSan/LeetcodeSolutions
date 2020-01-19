def decompressRLElist(self, nums: List[int]) -> List[int]:
    r = []
    for i in range(0, len(nums)-1, 2):
        for k in range(nums[i]):
            r.append(nums[i+1])
    return r