from hashlib import md5

s = input()

ans = 1
while True:
    if md5((s + str(ans)).encode()).hexdigest()[:6] == '000000':
        print(ans)
        break
    ans += 1
