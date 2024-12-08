from collections import defaultdict

before = defaultdict(set)

for i in range(1176):
    a, b = map(int, input().split('|'))
    before[a].add(b)
input()

ans = 0

for i in range(202):
    s = list(map(int, input().split(',')))[::-1]
    p = set(s)
    for i in s:
        p.remove(i)
        tocheck = p.intersection(before[i])
        if tocheck:
            break
    else:
        ans += s[len(s)//2]

print(ans)
