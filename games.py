x = int(input())
away, home, c = [], [], 0
for i in range(x):
    y = list(map(int, input().split(' ')))
    home.append(y[0])
    away.append(y[1])
for i in home:
    for j in away:
        if i == j: c = c+1
print(c)
