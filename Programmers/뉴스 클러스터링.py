def solution(str1, str2):
    jakad = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    A = []
    B = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            A.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            B.append(str2[i]+str2[i+1])
    # 공집합
    if not A and not B: return 65536
    
    intersection = set(A) & set(B)
    union = set(A) | set(B)
    
    multi_intersection = sum([min(A.count(inter), B.count(inter)) for inter in intersection])
    multi_union = sum([max(A.count(uni), B.count(uni)) for uni in union])
    
    jakad = int(multi_intersection/multi_union * 65536)
    return jakad