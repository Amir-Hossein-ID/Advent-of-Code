ans = 0
for i in range(16): # no of lines of input
    a = list(map(int, input().split()))
    ans += max(a) - min(a)

print(ans)
