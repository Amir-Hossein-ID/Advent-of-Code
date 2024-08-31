ans = 0
for i in range(16): # no of lines of input
    a = list(map(int, input().split()))
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            aa = a[i] / a[j]
            if aa == int(aa):
                ans += int(aa)
                break
            aa = a[j] / a[i]
            if aa == int(aa):
                ans += int(aa)
                break
        else:
            continue
        break

print(ans)
