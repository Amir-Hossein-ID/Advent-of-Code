s = input().split()
row = int(s[-3].strip(','))
col = int(s[-1].strip('.'))

nth = ((row - 1) ** 2 + (row - 1) + 2) // 2

for i in range(col - 1):
    row += 1
    nth += row

first = 20151125
power = 252533
remind = 33554393

ans = 1

nth -= 1

while nth:
    ans *= power
    ans %= remind
    nth -= 1

ans *= first
ans %= remind

print(ans)
