a = input()
ans = 0
last = a[-1]
i = -1
while i < len(a) - 1:
    if a[i] == a[i + 1]:
        ans += int(a[i])
    i += 1

print(ans)
