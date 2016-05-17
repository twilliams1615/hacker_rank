import math

## Find angle of MBC in degrees
## https://www.hackerrank.com/challenges/find-angle

AB = float(input())
BC = float(input())

if AB > 0 and AB <= 100 and BC > 0 and BC <= 100:
    AC = math.sqrt(AB**2 + BC**2)
    M = AC / 2.0
    aMBC = int(round(math.asin(AB/AC) * 180 / math.pi))
    print str(aMBC) + "°"
else:
    pass
