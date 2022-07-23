x = int(input())
s = input()
c = 0
try:
    for i in range(len(s)):
        if s[i+1] == s[i]:
            c = c+1
except:
    ValueError
print(c)
