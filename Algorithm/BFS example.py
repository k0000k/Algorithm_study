#147p BFS 예제

'''
BFS(깊이 우선 탐색)는 큐 자료구조를 사용하는 그래프 탐색 알고리즘이다.
1. 시작 노드를 큐에 넣는다
2. 해당 노드를 큐에서 꺼내고 인접 노드중에 방문하지 않은 노드를 모두 큐에 삽입한다.
3. 위 과정을 반복한다.
'''

from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결 된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결 된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문 된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의 된 BFS함수 호출
bfs(graph, 1, visited)

