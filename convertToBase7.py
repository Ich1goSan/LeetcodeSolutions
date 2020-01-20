def convertToBase7(self, num: int) -> str:
    n = abs(num)
    r =  ''
    while n:
        r = str(n % 7) + r
        n //= 7   
            
    return '-' + r if num < 0 else "0" if r == '' else r