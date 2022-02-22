S = input()
result = int(S[0])

for i in range(1, len(S)):
    next = int(S[i])
    if result >= 2 and next >= 2:  # 곱셈
        result *= next
    else:  # 두 숫자 중애 0과 1이 하나라도 있으면 덧셈이 더 큼
        result += next
    print(result)
