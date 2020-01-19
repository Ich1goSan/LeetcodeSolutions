def moveZeroes(self, nums: List[int]) -> None:
    k = 0
        
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[k] = nums[i]
            k+=1
                
    for i in range(k, len(nums)):
        nums[i] = 0