global N_list


def binary_search(N, key):
    global N_list

    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if key < N_list[mid]:
            end = mid - 1
        elif key > N_list[mid]:
            start = mid + 1
        else:  # x==mid
            return 1
    return 0


def solution():
    global N_list
    N = int(input())
    N_list = list(map(int, input().split()))
    N_list.sort()

    M = int(input())
    M_list = list(map(int, input().split()))

    for x in M_list:
        print(binary_search(N, x))


if __name__ == "__main__":
    solution()
