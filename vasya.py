
p = int(input())
lst, c = [], 0
for i in range(p):
    x, y = list(map(int, input().split(' ')))
    if x == 0 and y == 0:
        lst.append(1)
    elif x == 0 and y != 0:
        lst.append(1)
    else:
        lst.append(x+2*y+1)
for i in range(len(lst)):
    print(lst[i])
