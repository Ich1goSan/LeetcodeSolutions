def heightChecker(self, heights: List[int]) -> int:
    sortedH = sorted(heights)
    r = 0
    for i in range(len(heights)):
        if(heights[i] != sortedH[i]):
            r+=1
    return r