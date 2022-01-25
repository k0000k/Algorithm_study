#110p 구현 예제 상하좌우

#풀면서 이게 맞나... 싶었지만 반복을 해결할 해결책이 떠오르지 않았다ㅠㅠ

n = int(input())
road = list(input().split())

x = 1
y = 1

for i in road:
    if i == 'L':
        y -= 1
    elif i == 'R':
        y += 1
    elif i == 'U':
        x -= 1
    else:
        x += 1

    if y == 0:
        y = 1
    if y == n+1:
        y = n
    if x == 0:
        x = 1
    if x == n+1:
        x = n
print("%d %d"%(x,y))
