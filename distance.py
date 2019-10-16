import math
from math import sqrt

def distance(x1,y1,x2,y2):
    result = sqrt((x2 - x1)**2+(y2 - y1)**2)
    return float(("%.4f" %result)) if float(result) < 10000 else 'INFINITY'

case = input()
response = []
while int(case) != 0:
    points, result = [], []
    for i in range(0,int(case),1):
        numbers = input().split()
        coords = [float(numbers[0]), float(numbers[1])]
        points.append(eval('coords'))
    size = len(points)
    for i in range(0,size-1,1):
        for x in range(i+1,len(points),1):
            result.append(float(distance(points[i][0],points[i][1],points[x][0],points[x][1])))
    minvalue = min(result)
    response.append("%.4f" %float(minvalue) if minvalue != math.inf else 'INFINITY')
    case = input()

print(*response, sep = "\n") 