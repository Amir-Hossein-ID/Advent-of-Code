ans = 0
for i in range(1000):
    a,b,c = map(int, input().split('x'))
    d = [a*b, b*c, a*c]
    ans += 2 * sum(d) + min(d)
print(ans)
