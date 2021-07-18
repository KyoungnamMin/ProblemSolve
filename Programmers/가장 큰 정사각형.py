def solution(board):
    answer = 0
    if len(board)==1 and len(board[0])==1:
        if 0 in board: return 0
        else: return 1
        
    for i in range(1, len(board)):
        for j in range(1, len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j], board[i][j-1], board[i-1][j-1]) + 1
                if board[i][j] > answer:
                    answer = board[i][j]
    
    return answer ** 2