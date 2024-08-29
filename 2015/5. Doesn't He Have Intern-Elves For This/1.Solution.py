ans = 0
vowel = 'aeiou'

for i in range(1000):
    s = input()
    last = ''
    vc = 0
    dc = 0
    pc = 0
    for j in s:
        if vc < 3 and j in vowel:
            vc += 1
        if not dc and j == last:
            dc = 1
        if (last+j) in [('a','b'), ('c', 'd'), ('p', 'q'), ('x', 'y')]:
            pc = 1
            break
        last = j
    if vc>=3 and dc == 1 and pc == 0:
        ans += 1

print(ans)
