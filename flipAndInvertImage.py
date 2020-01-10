def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
    return [[j ^ 1 for j in i[::-1]] for i in A]