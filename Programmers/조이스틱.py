def solution(name):
    name = list(name)
    temp = ['A'] * len(name)
    change_alpha = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    
    answer = 0
    i = 0
    while True:
        # 글자 바꾸기
        if name[i] != 'A':
            answer += change_alpha[i]
            temp[i] = name[i]
        # 탈출 조건
        if name == temp:
            break
        # 커서 이동
        else:
            for move in range(len(name)):
                # 오른쪽으로 이동이 빠르다면 오른쪽으로 이동하고 이동횟수 반영
                if name[(i + move) % len(name)] != temp[(i + move) % len(name)]:
                    i = (i + move) % len(name)
                    answer += move
                    break
                # 왼쪽으로 이동이 빠르다면 왼쪽으로 이동하고 이동횟수 반영
                elif name[(i + len(name) - move) % len(name)] != temp[(i + len(name) - move) % len(name)]:
                    i = (i + len(name) - move) % len(name)
                    answer += move
                    break
                    
    return answer