x = int(input())
y = list(map(int, input().split(' ')))
sorted(y, reverse=True)
odd = []
even = []
for i in range(0, len(y)):
    if i % 2:
        even.append(y[i])
    else:
        odd.append(y[i])

print(sum(even), sum(odd))
