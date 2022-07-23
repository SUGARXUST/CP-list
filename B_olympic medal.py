x = list(map(int, input().split()))
x = max(x[1::])


p1 = list(map(int, input().split()))
p1 = max(p1[1::])


p2 = list(map(int, input().split()))
p2 = min(p2[1::])


m1, m2 = map(int, input().split())

ans = (x**2)
ans = ans*(1/((m1/m2)*(p2/p1)+1))
ans = ans**0.5

print(ans)
