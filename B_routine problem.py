from math import gcd
from fractions import Fraction

a, b, c, d = list(map(int, input().split()))
if a * d > b * c:
    p = a * d - b * c
    q = a * d
else:
    p = b * c - a * d
    q = b * c
print(Fraction(p, q)) if Fraction(p, q) > 0 else print("0/1")
