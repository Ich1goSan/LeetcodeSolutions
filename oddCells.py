def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
    matrix = [[0 for i in range(m)] for j in range(n)]
    for k in indices:
        for j in range(m):
            matrix[k[0]][j]+=1
        for s in range(n):
            matrix[s][k[1]]+=1
    result = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] & 1:
                result += 1
    return result