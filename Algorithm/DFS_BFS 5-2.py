#152p BFS 실전문제 5-2

from collections import deque

n, m = map(int, input().split())

maze = []

for i in range(n):
    maze.append(list(map(int, input())))

# 이동 방향 미리 저장
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 실행
    while queue:
        x, y = queue.popleft()
        
        # 동서남북 반복
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 미로 범위 벗어나면 그 이동은 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue 
            # 갈 수 없는 칸이면 이동 무시
            if maze[nx][ny] == 0:
                continue
            # 최초 방문시에만 카운트 1 증가
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    # 도착 칸의 카운트 출력
    return maze[n-1][m-1]

print(bfs(0, 0))
