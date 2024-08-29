from hashlib import md5

s = input()

ans = 1
while True:
    if md5((s + str(ans)).encode()).hexdigest()[:5] == '00000':
        print(ans)
        break
    ans += 1
