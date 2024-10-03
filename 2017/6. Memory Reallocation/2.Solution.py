a = list(map(int, input().split()))

ans = 0

seen = {tuple(a):0}

while True:
    ind = max(range(len(a)), key= lambda x: a[x])
    temp = a[ind]
    a[ind] = 0
    while temp:
        ind += 1
        ind %= len(a)
        a[ind] += 1
        temp -= 1
    ans += 1
    if tuple(a) in seen:
        break
    seen[tuple(a)] = ans

print(ans - seen[tuple(a)])
