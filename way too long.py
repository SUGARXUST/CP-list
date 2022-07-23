t = int(input())
for i in range(t):
    s = input()
    a = s[0]+str(len(s)-2)+s[-1] if len(s) > 10 else s
    print(a)
