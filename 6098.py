#6098 : [기초-리스트] 성실한 개미(py)

d = [[0] for i in range(11)]
for i in range(1,11):
    x=input().split()
    d[i].extend(x)

for i in range(1,11):
    for j in range(1,11):
        d[i][j]=int(d[i][j])

x=2
y=2
d[x][y]=9

while True:
    if d[x][y+1]==2:
        d[x][y+1]=9
        break
    elif d[x][y+1]==0:
        d[x][y+1]=9
        y=y+1
        continue
    elif d[x+1][y]==2:
        d[x+1][y]=9
        break
    elif d[x+1][y]==0:
        d[x+1][y]=9
        x=x+1
        continue
    else:
        break
for i in range(1,11):
    for j in range(1,11):
        print(d[i][j],end=' ')
    print('')
