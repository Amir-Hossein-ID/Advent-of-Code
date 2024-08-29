ans = 0

for i in range(300):
    s = input()
    x = len(s)
    y = len(s) + 3

    i = 1
    while i != x:
        if s[i] in '\\"':
            y += 1
        i += 1
    ans += y - x

print(ans)
