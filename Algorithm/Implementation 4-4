#118p 구현 실전문제 게임개발

#문제를 잘 읽고 이해하자. 처음 캐릭터가 위치한 곳이 육지인걸... 너무 늦게 눈치챘다.

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

gamemap=[]
move = [1, -1]

#방문한 위치 저장을 위한 맵을 따로 생성하여 초기화
#리스트 컴프리헨션을 이용하여 효율적인 리스트 생성
#언더바 사용은 변수 무시를 위해서!
d = [[0] * m for _ in range(n)]

d[x][y] = 1 #현재좌표 방문처리

for i in range(n):
    gamemap.append(list(map(int, input().split())))

#북, 동, 서, 남 방향 정의
#directuon 값을 dx, dy의 인덱스 값으로 사용
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

#시뮬레이션 시작
count = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    #회전 이후 정면에 가보지 않은 칸이 존재하는 경우
    #이동 예정인 칸이 아직 방문 X and 맵이 육지
    if d[nx][dy] == 0 and gamemap[nx][ny] == 0:
        d[nx][dy] == 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else:
        turn_time += 1

    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있으면 이동
        if gamemap[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다일때
        else:
            break
        turn_time = 0

print(count)

