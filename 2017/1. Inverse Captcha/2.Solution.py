a = input()
ans = 0
next = len(a) // 2

for i in range(len(a)):
    new = (i + next) % len(a)
    if a[i] == a[new]:
        ans += int(a[i])

print(ans)
