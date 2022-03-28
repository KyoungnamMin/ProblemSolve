def get_key(dic, val):
    for key, value in dic.items():
        if val == value:
            return key
    return "key doesn't exist"


def sliding_window(strs):
    n = len(strs)
    if n < l:
        return n
    idx = 0
    ridx, lidx = 0, 0
    maxi = 0
    dic = dict()

    while ridx < n:
        if len(dic) < k:
            dic[strs[ridx]] = ridx
            ridx += 1
        if len(dic) == k:
            mini = min(dic.values())
            del dic[get_key(dic, mini)]
            lidx = mini + 1
        maxi = max(maxi, ridx - lidx)

    return maxi


print(sliding_window("ABBBBBBBBBBBCDDDDD"))
