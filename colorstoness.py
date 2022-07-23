a, b = list(input() for i in range(2))
z = 0
for i in b:
    if i == a[z]:
        z += 1
print(z+1)
