from hashlib import md5

n = input()
num = 0

password_len = 0

while password_len != 8:
    hash = md5((n + str(num)).encode()).hexdigest()
    if hash[:5] == '00000':
        password_len += 1
        print(hash[5], end='')
    num += 1
