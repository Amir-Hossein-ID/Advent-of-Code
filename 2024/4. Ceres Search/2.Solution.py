a = [input() for i in range(140)]

ans = 0
visited_mas = set()

for i, j in enumerate(a):
    for k, p in enumerate(j):
        if p == 'M':
            kinds = []
            if k < len(j) - 2 and i < len(a) - 2:
                if a[i+1][k+1] + a[i+2][k+2] == 'AS':
                    kinds.append((i+1, k+1))
            if k < len(j) - 2 and i > 1:
                if a[i-1][k+1]+a[i-2][k+2] == 'AS':
                    kinds.append((i-1, k+1))
            if k > 1 and i < len(a) - 2:
                if a[i+1][k-1]+a[i+2][k-2] == 'AS':
                    kinds.append((i+1, k-1))
            if k > 1 and i > 1:
                if a[i-1][k-1]+a[i-2][k-2] == 'AS':
                    kinds.append((i-1, k-1))
            for p in kinds:
                if p in visited_mas:
                    ans += 1
                else:
                    visited_mas.add(p)

print(ans)
