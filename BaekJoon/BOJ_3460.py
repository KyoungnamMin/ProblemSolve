import sys
import re

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    answer = []
    n = int(input())
    bin_n = str(format(n, "b"))
    print(bin_n)
