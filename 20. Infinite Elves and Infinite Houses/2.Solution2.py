n = int(input())

i = 2
ans = 1
while ans * 11 < n:
    i += 2
    ans = set()
    for j in range(1, int(i**(1/2) + 1)):
        if i % j == 0:
            asd = i//j
            if j*50 >= i:
                ans.add(j)
            if asd*50 >= i:
                ans.add(asd)
    ans = sum(ans)

print(i)
