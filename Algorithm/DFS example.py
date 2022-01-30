#142p DFS 예제

'''
DFS(깊이 우선 탐색)는 스택 자료구조를 사용하는 그래프 탐색 알고리즘이다.
1. 탐색 시작 노드를 스택에 넣고 방문처리 한다.
2. 스택의 최상단 노드에 인접한 미방문 노드가 있으면 스택에 넣고 방문처리 한다.
3. 인접한 노드에 모두 방문했으면 그 최상단 노드를 스택에서 꺼낸다.
4. 위 과정을 반복한다.
'''

# DFS 메서드 정의
def dfs(gragh, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결 된 다른 노드를 재귀적으로 방문
    for i in gragh[v]:
        if not visited[i]:
            dfs(gragh, i, visited)


# 각 노드가 연결 된 정보를 리스트 자료형으로 표현 (2차원 리스트)
# 2, 3, 8 이런식으로 작은 숫자의 노드부터 들어가 있어서 방문도 이 순서로 이루어짐!
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

dfs(graph, 1, visited)
