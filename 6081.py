#6081 : [기초-종합] 16진수 구구단 출력하기(py)

n=input()
h=int(n,16)
for i in range(1,16):
    print('%X'%h,'*%X'%i,'=%X'%(h*i),sep='')
