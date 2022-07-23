n = int(input())
l = list(map(int, input().split()))
hire = 0
count = 0
for i in range(len(l)):
    if l[i] > 0:
        hire = hire+l[i]
    if l[i] == -1:
        if hire == 0:
            count += 1
        else:
            hire = hire-1
print(count)
