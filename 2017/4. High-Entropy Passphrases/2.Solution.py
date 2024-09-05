ans = 0
for i in range(512): # no of lines of input
    phrase = ["".join(sorted(i)) for i in input().split()]
    if len(phrase) == len(set(phrase)):
        ans += 1

print(ans)
