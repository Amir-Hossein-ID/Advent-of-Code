n = int(input())

s = 1
while n > s * s:
    s += 2

if n == s * s:
    ans = s - 1
    print(ans)
    exit()

ans = s // 2

candid = s * s - s // 2
while abs(n - candid) > s // 2:
    candid -= s - 1

ans += abs(n - candid)
print(ans)
