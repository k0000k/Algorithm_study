#6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)

n=int(input())
a=input().split()
for i in range(n):
    a[i]=int(a[i])
a.sort()
print(a[0])
