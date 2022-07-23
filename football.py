n = int(input())
x = [input() for j in range(n)]
team = [i for i in set(x)]
print(team)
score = [x.count(i) for i in team]
print(score)
print(team[score.index(max(score))])
