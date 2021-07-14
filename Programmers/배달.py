import heapq

def dijkstra(start, graph, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        #print(q)
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(N, road, K):
    INF = int(1e9)
    distance = [INF] * (N+1)
    graph = [[] for i in range(N+1)]
    for x, y, z in road:
        graph[x].append((y, z))
        graph[y].append((x, z))
    
    dijkstra(1, graph, distance)
    
    count = 0
    for d in distance:
        if d <= K:
            count += 1

    return count