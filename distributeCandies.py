def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    r = [0 for _ in range(num_people)]
    i = 0
    c = 1
    while candies != 0:
        if i > num_people - 1:
            i = 0
        if c > candies:
            r[i] += candies
            break
        r[i] += c
        candies -= c
        i += 1
        c += 1
    return r
    