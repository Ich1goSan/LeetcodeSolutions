def plusOne(self, digits: List[int]) -> List[int]:
    r = "".join([str(i) for i in digits])
    return list(map(int, list(str(int(r) + 1))))