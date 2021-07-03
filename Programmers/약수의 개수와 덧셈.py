'''
def get_divisor_count(n):
    count = 0
    for i in range(1, int(n**(1/2))+1):
        if n%i == 0:
            if n**(1/2) == i: count += 1
            else: count += 2
    return count
''' 

def solution(left, right):
    answer = 0
    
    for num in range(left, right+1):
        if int(num**0.5) == num**0.5:
            answer -= num
        else:
            answer += num
        '''
        num_divisor_count = get_divisor_count(num)
        if num_divisor_count%2 == 0: answer += num
        else: answer -= num
        '''
    
    return answer