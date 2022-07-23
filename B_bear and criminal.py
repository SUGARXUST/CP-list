# INPUT
n, a = map(int, input().split())
ls = list(map(int, input().split()))

l = r = a-1
counter = 0
# frist check if there are criminal in city that he live
if ls[a-1] == 1:
    counter += 1

while l >= 0 or r < n:
    l -= 1
    r += 1
    # if there are cities in left and right
    if l >= 0 and r < n:
        if ls[l] == 1 and ls[r] == 1:
            counter += 2
    # if there are cities in left only
    elif l >= 0:
        if ls[l] == 1:
            counter += 1
    # if there are cities in right only
    elif r < n:
        if ls[r] == 1:
            counter += 1

# output
print(counter)
