n = int(input())

l = list(range(1, n+1))

while len(l) > 1:
    l = (l[-1:] if len(l) % 2 else []) + l[:-1:2]
    print(l)

print(l)
