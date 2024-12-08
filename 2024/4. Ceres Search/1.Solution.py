a = [input() for i in range(140)]

ans = 0

for i, j in enumerate(a):
    for k, p in enumerate(j):
        if p == 'X':
            kinds = []
            if k < len(j) - 3:
                kinds.append(j[k+1]+j[k+2]+j[k+3])
            if k > 2:
                kinds.append(j[k-1]+j[k-2]+j[k-3])
            if i < len(a) - 3:
                kinds.append(a[i+1][k]+a[i+2][k]+a[i+3][k])
            if i > 2:
                kinds.append(a[i-1][k]+a[i-2][k]+a[i-3][k])
            if k < len(j) - 3 and i < len(a) - 3:
                kinds.append(a[i+1][k+1]+a[i+2][k+2]+a[i+3][k+3])
            if k < len(j) - 3 and i > 2:
                kinds.append(a[i-1][k+1]+a[i-2][k+2]+a[i-3][k+3])
            if k > 2 and i < len(a) - 3:
                kinds.append(a[i+1][k-1]+a[i+2][k-2]+a[i+3][k-3])
            if k > 2 and i > 2:
                kinds.append(a[i-1][k-1]+a[i-2][k-2]+a[i-3][k-3])
            ans += sum(i == 'MAS' for i in kinds)

print(ans)
