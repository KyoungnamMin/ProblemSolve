# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
def solution1():
    from queue import PriorityQueue

    # 우선순위 큐 방법
    N = int(input())
    que = PriorityQueue()

    for _ in range(N):
        x = int(input())
        que.put(x)
    while not que.empty():
        print(que.get())


def solution2():
    # 그냥 배열 정렬 방법
    N = int(input())
    array = []
    for _ in range(N):
        x = int(input())
        array.append(x)
    array.sort()
    for value in array:
        print(value)


if __name__ == "__main__":
    solution1()
    solution2()
