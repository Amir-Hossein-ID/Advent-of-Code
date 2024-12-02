a = []
b = []
for i in range(1000):
    c = input().split()
    a.append(int(c[0]))
    b.append(int(c[1]))

a.sort()
b.sort()

ans = 0

for i in range(1000):
    ans += abs(a[i] - b[i])

print(ans)
