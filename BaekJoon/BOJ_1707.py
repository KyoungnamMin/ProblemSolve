import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now, groupNum):
    visited[now] = groupNum
    for i in arr[now]:
        if visited[i] == 0:
            if not dfs(i, -groupNum):
                return False
        elif visited[i] == visited[now]:
            return False
    return True

T = int(input())
for _ in range(T):
    v, e = map(int, input().split())
    arr = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)
    for _ in range(e):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    result = True
    for i in range(1, v+1):
        if visited[i] == 0:
           result = dfs(i, 1)
           if not result:
               break
    if result: 
        print("YES")
    else: 
        print("NO")