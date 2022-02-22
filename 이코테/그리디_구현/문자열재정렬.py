s = input()

reorder = []
s_num = 0

for data in s:
    if data.isalpha():
        reorder.append(data)
    elif data.isdecimal():
        s_num += int(data)

reorder.sort()

if s_num != 0:
    reorder.append(str(s_num))

answer = "".join(reorder)
print(answer)
