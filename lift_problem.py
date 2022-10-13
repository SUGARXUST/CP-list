dist1 = dist2 = 0

for i in range(int(input())):
    l = []
    l = list(map(int, input().split(" ")))

    dist1 = l[0] - 1

    dist2 = abs(l[2] - l[1])

    if l[2] != 1:
        dist2 += l[2] - 1

    if dist1 > dist2:
        print(2)

    elif dist2 > dist1:
        print(1)

    else:
        print(3)