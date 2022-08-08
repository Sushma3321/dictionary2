s="sushma"
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i]=d[i]+1
for j in range(len(s)):
    if d[s[j]]== 1:
        print(s[j],":",j)
        break
else:
    print(-1)



