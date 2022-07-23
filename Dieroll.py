from fractions import Fraction
x = max(list(map(int, input().split(' '))))
y = 7-x
prob = Fraction(y, 6)
if prob < 1:
    print(prob)
if prob == 1:
    print("1/1")
if prob == 0:
    print("0/1")
