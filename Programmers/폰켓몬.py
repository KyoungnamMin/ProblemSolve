def solution(nums):
    set_n = len(set(nums))
    get_n = len(nums)//2
    if set_n <= get_n:
        answer = set_n
    else:
        answer = get_n
    
    return answer