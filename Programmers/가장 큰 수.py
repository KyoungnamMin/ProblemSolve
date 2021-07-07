def solution(numbers):
    array = list(map(str, numbers))
    array.sort(reverse=True, key=lambda x: (x*3)[:4])
    
    answer = ''.join(array)
    return answer if answer[0] != '0' else '0'