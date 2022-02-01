#151p DFS/BFS 실전문제 5-1

'''
고민해도 모르겠어서... 예시 코드 보고 공부... 아래 적은 부분은 이해하는데 오래 걸린 부분 정리
- 0인 칸이 1개라도 있으면 그때부터 카운트 한다.
- 현재 칸에서 상하좌우 방문 안한 칸을 계속 방문 할 수 있을 때 까지 진행
- 방문처리(0->1) = 방문 불가한 칸(1)
'''

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정 노드를 방문하고, 상하좌우 연결 된 모든 노드를 재귀적으로 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문 하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x - 1, y)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        # 0,0 이 탐색 시작점. 만약 0,0이 방문 가능하면 True를 리턴해서 if문이 실행되고, 이때 0,0과 인접한 칸은 모두 1로 바뀌어있음.
        if dfs(i, j) == True:
            result += 1

print(result)
