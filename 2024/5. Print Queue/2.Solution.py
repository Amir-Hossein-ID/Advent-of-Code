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
        continue

    while True:
        p = set(s)
        for j,i in enumerate(s):
            p.remove(i)
            tocheck = p.intersection(before[i])
            if tocheck:
                aa = s.index(tocheck.pop())
                s[j], s[aa] = s[aa], s[j]
                break
        else:
            ans += s[len(s)//2]
            break


print(ans)
