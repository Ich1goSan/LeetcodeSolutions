def binarySearch(self, arr, l, r, x): 
        while l <= r: 
            mid = l + (r - l)//2; 
            if arr[mid] == x: 
                return mid 
            elif arr[mid] < x: 
                l = mid + 1
            else: 
                r = mid - 1
        return -1
    
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    for i in range(len(numbers)):
        diff = target - numbers[i]
        ind = self.binarySearch(numbers, 0, len(numbers)-1, diff)
        if ind != -1:
            if ind == i:
                return [i+1, ind+2]
            return [i+1, ind+1]