"""
코딩테스트를 위한 알고리즘 정리
- BFS, DFS, 
"""


def bfs(graph, start, visited):
    from collections import deque

    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True


def main_bfs():
    graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
    visited = [False] * 9
    bfs(graph, 1, visited)


def dfs(graph, start, visited):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


def main_dfs():
    graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]
    visited = [False] * 9

    dfs(graph, 1, visited)
