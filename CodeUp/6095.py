#6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)

d = [[0 for j in range(20)] for i in range(20)]
n=int(input())
for i in range(n) :
  x, y = input().split()
  d[int(x)][int(y)] = 1
for i in range(1,20):
    for j in range(1,20):
        d[i][j]=int(d[i][j])
        print(d[i][j],end=' ')
    print('')
