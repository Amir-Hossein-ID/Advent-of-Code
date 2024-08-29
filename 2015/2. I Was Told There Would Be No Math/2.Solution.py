ans = 0
for i in range(1000):
    dimentions = sorted(map(int, input().split('x')))
    ans += 2 * dimentions[0] + 2 * dimentions[1]+ dimentions[0] * dimentions[1] * dimentions[2]
print(ans)
