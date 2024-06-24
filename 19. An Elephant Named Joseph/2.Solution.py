from math import log

n = int(input())
high = int(log(n, 3))
high3 = 3**high
l = n - high3

if l:
    if l <= high3:
        print(l)
    else:
        ll = l - high3
        print(high3 + ll * 2)
else:
    print(n)

# got this by looking at the first 100 results :D
