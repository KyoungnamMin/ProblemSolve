def solution(a, b):
    month_day = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    
    mydays = 0
    for i in range(a-1):
        mydays += month_day[i]
    mydays += b
    
    while mydays>=7:
        mydays = mydays%7
    
    return days[mydays-1]