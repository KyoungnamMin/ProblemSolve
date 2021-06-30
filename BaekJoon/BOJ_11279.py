import heapq
def heapsort_max(iterable):
    h = []
    for value in iterable:
        if value == 0:
            if not h:
                print(0)
            else:
                print(-heapq.heappop(h))
        else:
            heapq.heappush(h, -value)

N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

heapsort_max(array)