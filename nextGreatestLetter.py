def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    l = 0
    r = len(letters) - 1

    if target >= letters[-1]:
        return letters[0]

    while l < r:
        mid = l + (r - l) // 2
        if letters[mid] > target:
            r = mid
        else:
            l = mid + 1
    return letters[l]
