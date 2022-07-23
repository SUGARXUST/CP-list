n = int(input())
a = list(map(int, input().split()))

d = {}
for i in range(len(a)):
    if a[i] not in d:
        d[a[i]] = [i]
    else:
        d[a[i]].append(i)
print(d)
ans = []
for i, j in d.items():
    if len(j) == 1:
        ans.append([i, 0])
        continue
    s = set()
    for k in range(1, len(j)):
        s.add(j[k] - j[k - 1])
        print(s)
    if len(s) == 1:
        ans.append([i, list(s)[0]])
        print(ans)
print(ans)
ans.sort()
print(ans)
print(len(ans))
for i, j in ans:
    print(i, j)
