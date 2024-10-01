j = []

for i in range(1056): # no of lines of input
    j.append(int(input()))

ans = 0

ind = 0
while ind < len(j) and ind >= 0:
    temp = ind + j[ind]
    if j[ind] >= 3:
        j[ind] -= 1
    else:
        j[ind] += 1

    ind = temp
    ans += 1

print(ans)
