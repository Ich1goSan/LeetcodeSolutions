def findComplement(self, num: int) -> int:
        x = bin(num)[2:]
        z = ""
        
        for i in x:
            z+=str(int(i) ^ 1)
            
        return int(z, 2)