ans = 0

def check(a):
    d = sorted(a)
    if d == a or d[::-1] == a:
        last = d[0] - 1
        for i in d:
            if i - last > 3 or i - last < 1:
                break
            last = i
        else:
            return True
    return False

for i in range(1000):
    a = list(map(int, input().split()))
    it = check(a)
    it |= any(check(a[:i] + a[i+1:]) for i in range(len(a)))
    ans += it

print(ans)
