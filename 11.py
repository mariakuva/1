import math
a = float(input())
b = float(input())
R = max(a, b)
r = min(a, b)
S = math.pi * (R ** 2 - r ** 2)
print(S)
