
n = list(map(int, input().split()))
s = input()
calories = 0
for i in range(len(s)):
    if s[i] == '1':
        calories += n[0]
    elif s[i] == '2':
        calories += n[1]
    elif s[i] == '3':
        calories += n[2]
    else:
        calories += n[3]

print(calories)
