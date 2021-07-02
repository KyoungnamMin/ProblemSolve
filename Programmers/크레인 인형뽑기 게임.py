def solution(board, moves):
    answer = 0
    basket = []
    N = len(board)
    for crain in moves:
        for i in range(N):
            if board[i][crain-1] != 0:
                basket.append(board[i][crain-1])
                board[i][crain-1] = 0
                break
        if len(basket) >= 2 and basket[-1] == basket[-2]:
            basket.pop()
            basket.pop()
            answer += 2
        
    return answer