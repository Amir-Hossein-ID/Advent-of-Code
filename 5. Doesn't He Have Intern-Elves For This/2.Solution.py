ans = 0

for i in range(1000):
    s = input()
    last1 = ''
    last2 = ''
    pair = False
    reap = False
    for k in range(len(s)):
        j = s[k]
        if j == last2:
            reap = True
        if last1 and last1+j in s[k+1:]:
            pair = True
        if reap and pair:
            ans += 1
            break
        last2 = last1
        last1 = j

print(ans)
