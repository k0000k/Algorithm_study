#97p 그리디 예제 3-3 거스름돈

num = []

n, m = map(int, input().split())

for i in range(n):
    temp = list(map(int, input().split()))
    num.append(min(temp))
print(max(num))
