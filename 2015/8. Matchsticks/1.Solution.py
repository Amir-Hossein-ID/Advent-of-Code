ans = 0

for i in range(300):
    s = input()
    x = len(s)
    y = 0

    i = 1
    while s[i] != '"':
        if s[i] == '\\':
            if s[i+1] == '\\' or s[i+1] == '"':
                i += 1
            else:
                i += 3
        y += 1
        i += 1
    ans += x - y

print(ans)
