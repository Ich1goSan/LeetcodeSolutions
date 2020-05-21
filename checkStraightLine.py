def checkStraightLine(self, coordinates):
    if len(coordinates) == 2:
        return True
    firstProduct = self.crossProduct(coordinates[0], coordinates[1])
    for i in range(1, len(coordinates)-1):
        currentProduct = self.crossProduct(coordinates[i], coordinates[i+1])
        if firstProduct != currentProduct:
            return False
    return True


def crossProduct(self, point1, point2):
    a = (point1[0]-point2[0])
    if a == 0:
        return 0
    slope = (point1[1]-point2[1])/a
    return slope
    
