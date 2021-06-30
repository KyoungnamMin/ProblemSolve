n = int(input())

list_n = [0, 1, 2]

for i in range(3, n+1):
    list_n.append(list_n[i - 2] + list_n[i - 1])

print(list_n[n] % 10007)