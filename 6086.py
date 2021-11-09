#6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)

n=int(input())
sum=0
i=1
while True:
    sum=sum+i
    i=i+1
    if sum>=n:
        print(sum)
        break
