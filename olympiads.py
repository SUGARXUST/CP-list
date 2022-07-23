n = int(input())
t = list(map(int, input().split()))
prog = []
math = []
fizra = []
for i in range(n):
    if t[i] == 1:
        prog.append(i + 1)
    elif t[i] == 2:
        math.append(i + 1)
    else:
        fizra.append(i + 1)
teams = min(len(prog), len(math), len(fizra))
print(teams)
for i in range(teams):
    print(prog[i], math[i], fizra[i])
