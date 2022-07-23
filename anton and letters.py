set = input()
set = set.replace("{", "").replace("}", "").replace(", ", "")
t = ""
for i in set:
    if(i in t):
        pass
    else:
        t = t+i
print(len(t))
