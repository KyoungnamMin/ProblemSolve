def solution(n, arr1, arr2):
    # 주어진 arr1과 arr2를 2진수로 변환
    # 변환된 값을 OR 연산한 뒤, '#'과 ' '으로 변환
    answer = []
    for i in range(n):
        arr1[i] = format(arr1[i], 'b')
        arr2[i] = format(arr2[i], 'b')
        if len(arr1[i]) < n:
            arr1[i] = '0'*(n-len(arr1[i]))+str(arr1[i])
        if len(arr2[i]) < n:
            arr2[i] = '0'*(n-len(arr2[i]))+str(arr2[i])
        
        tmp = ''
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)

    return answer