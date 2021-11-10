#6097 : [기초-리스트] 설탕과자 뽑기(py)

h,w=input().split()

h=int(h)
w=int(w)

cross=[[0 for i in range(w+1)]for i in range(h+1)]

n=int(input())

for i in range(n):
    l,d,x,y=input().split()

    l=int(l)
    x=int(x)
    y=int(y)

    if d=='0':
        for i in range(l):
            cross[x][y]=1
            y=y+1
    else:
        for i in range(l):
            cross[x][y]=1
            x=x+1
for i in range(1,h+1):
    for j in range(1,w+1):
        cross[i][j]=int(cross[i][j])
        print(cross[i][j],end=' ')
    print('')
