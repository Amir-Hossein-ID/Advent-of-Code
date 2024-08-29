from hashlib import md5

n = input()
num = 0

password = [False] * 8
length = 0

while not all(password):
    hash = md5((n + str(num)).encode()).hexdigest()
    if hash[:5] == '00000':
        if int(hash[5], 16) < 8 and not password[int(hash[5])]:
            password[int(hash[5])] = hash[6]
            print(".", end='') # decrypting "animation" LOL
    num += 1

print()
print(''.join(password))
