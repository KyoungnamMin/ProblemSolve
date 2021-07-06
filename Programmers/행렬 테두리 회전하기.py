def solution(rows, columns, queries):
    answer = []
    board = [[(i-1)*columns+j for j in range(1, columns+1)] for i in range(1, rows+1)]
    
    for x1, y1, x2, y2 in queries:
        # 좌상단 값 저장: 값 변화 순서 = 좌 세로 -> 하 가로 -> 우 세로 -> 상 가로
        tmp = board[x1-1][y1-1]
        min_value = tmp
        # 좌 세로
        for k in range(x1-1, x2-1):
            board[k][y1-1] = board[k+1][y1-1]
            min_value = min(min_value, board[k+1][y1-1])
        # 하 가로
        for k in range(y1-1, y2-1):
            board[x2-1][k] = board[x2-1][k+1]
            min_value = min(min_value, board[x2-1][k+1])
        # 우 세로
        for k in range(x2-1, x1-1, -1):
            board[k][y2-1] = board[k-1][y2-1]
            min_value = min(min_value, board[k-1][y2-1])
        # 상 가로
        for k in range(y2-1, y1-1, -1):
            board[x1-1][k] = board[x1-1][k-1]
            min_value = min(min_value, board[x1-1][k-1])
        
        board[x1-1][y1] = tmp
        answer.append(min_value)    
    
    return answer