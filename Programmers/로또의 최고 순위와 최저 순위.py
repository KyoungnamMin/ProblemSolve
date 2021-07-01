def solution(lottos, win_nums):
    lotto_rate = [6, 6, 5, 4, 3, 2, 1]
    lotto_count = 0
    zero_count = lottos.count(0)
    
    if zero_count == 6: return [1, 6]
    if sorted(lottos) == sorted(win_nums): return[1, 1]
    
    for num in win_nums:
        if num in lottos:
            lotto_count += 1
    
    higher_rate = lotto_rate[lotto_count + zero_count]
    lower_rate = lotto_rate[lotto_count]
    
    return [higher_rate, lower_rate]