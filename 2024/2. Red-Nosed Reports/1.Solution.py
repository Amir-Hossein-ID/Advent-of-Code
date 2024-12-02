ans = 0
for i in range(1000):
    a = list(map(int, input().split()))
    d = sorted(a)
    if d == a or d[::-1] == a:
        last = d[0] - 1
        for i in d:
            if i - last > 3 or i - last < 1:
                break
            last = i
        else:
            ans += 1

print(ans)
