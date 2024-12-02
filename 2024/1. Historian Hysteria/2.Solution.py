a = []
b = []
for i in range(1000):
    c = input().split()
    a.append(int(c[0]))
    b.append(int(c[1]))

a.sort()
b.sort()

ans = 0

lastnum = -1
count = 0

bind = 0

for i in a:
    if i != lastnum:
        count = 0
    while bind < 1000 and b[bind] <= i:
        if b[bind] == i:
            count += 1
        bind += 1
    ans += count * i
    lastnum = i

print(ans)
