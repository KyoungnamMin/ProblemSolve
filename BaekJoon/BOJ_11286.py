import heapq
def heapsort_abs(iterable):
    h = []
    for value in iterable:
        if value == 0:
            if not h:
                print(0)
            else:
                print(heapq.heappop(h)[1])
        else:
            heapq.heappush(h, (abs(value), value))

N = int(input())
array = []
for _ in range(N):
    array.append(int(input()))

heapsort_abs(array)