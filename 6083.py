#6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)

r,g,b=map(int,input().split())
count=0
for i in range(r):
    for n in range(g):
        for m in range(b):
            print(i,n,m)
            count=count+1
print(count)
