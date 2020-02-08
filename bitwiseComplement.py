def bitwiseComplement(self, N: int) -> int:
    num = bin(N)[2:]
    return int(''.join([str(int(i) ^ 1) for i in num]), 2)
    