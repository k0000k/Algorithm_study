#6096 : [기초-리스트] 바둑알 십자 뒤집기(py)

d = [[0] for i in range(20)]
for i in range(1,20):
    x=input().split()
    d[i].extend(x)

for i in range(1,20):
    for j in range(1,20):
        d[i][j]=int(d[i][j])
        
n=int(input())

for i in range(n):
    x,y=input().split()
    for j in range(1, 20):
        if d[j][int(y)]==0:
            d[j][int(y)]=1
        else:
            d[j][int(y)]=0
            
    for j in range(1, 20):
        if d[int(x)][j]==0:
            d[int(x)][j]=1
        else:
            d[int(x)][j]=0
      
for i in range(1,20):
    for j in range(1,20):
        print(d[i][j],end=' ')
    print('')
