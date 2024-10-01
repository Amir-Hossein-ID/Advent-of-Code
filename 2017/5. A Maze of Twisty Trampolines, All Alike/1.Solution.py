j = []

for i in range(1056): # no of lines of input
    j.append(int(input()))

ans = 0

ind = 0
while ind < len(j) and ind >= 0:
    j[ind] += 1
    ind = ind + j[ind] - 1
    ans += 1

print(ans)
