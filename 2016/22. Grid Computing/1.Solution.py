input()
input()
data = [[0] * 27 for _ in range(37)] # no of input
for i in range(37):
    for j in range(27): #no of lines of input
        s = input().split()
        data[i][j] = [int(p[:-1]) for p in s[1:]]

ans = 0

for i in range(37):
    for j in range(27):
        if data[i][j][1] == 0:
            continue
        for p in range(37):
            for k in range(27):
                if i == p and k == j:
                    continue
                if data[i][j][1] <= data[p][k][2]:
                    ans += 1

print(ans)
