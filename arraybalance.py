
n = int(input())
ans = []
for i in range(n):
    x = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    sum_a = 0
    sum_b = 0
    for i in range(1, x):
        sum_a += abs((a[i]-a[i-1])) + abs((b[i]-b[i-1]))
        sum_b += abs((b[i]-a[i-1])) + abs((a[i]-b[i-1]))

    ans.append(min(sum_a, sum_b))
for i in ans:
    print(i)
