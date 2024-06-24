# https://www.youtube.com/watch?v=uCsD3ZGzMgE
from math import log2

n = int(input())
l = n - 2 ** int(log2(n))
print(2 * l + 1)
