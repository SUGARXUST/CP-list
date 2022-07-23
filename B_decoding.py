n = int(input())
s = input()
r = ''
# if(n % 2 == 1):
r = s[::2]
print(r)
a = s[1::2]
print(a)
r = a[::-1]+r
print(r)
# 'else:
#r = s[::2]
#r = r[::-1]
#r += s[1::2]
# print(r)
''
