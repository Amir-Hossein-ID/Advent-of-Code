vals = []
input_num = 4
for i in range(input_num): # no of lines of input
    inp = input().split()
    vals.append([int(inp[i*2].strip(",")) for i in range(1,6)])

def giveme(n, target):
    if n == 1:
        yield [target]
    else:
        for i in range(0, target + 1):
            for j in giveme(n-1, target - i):
                yield [i] + j

ans = 0
for i in giveme(input_num, 100):
    cur = 1
    for k in range(4):
        a = 0
        for j in range(len(vals)):
            a += i[j] * vals[j][k]
        a = 0 if a < 0 else a
        cur *= a
    if cur > ans:
        ans = cur
print(ans)
