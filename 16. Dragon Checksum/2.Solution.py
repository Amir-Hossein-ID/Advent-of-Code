inp = input()
disk = 35651584

while len(inp) < disk:
    inp = inp + '0' + inp[::-1].translate(str.maketrans('01', '10'))

inp = inp[:disk]

size = disk
ans = 1
while size % 2 == 0:
    ans *= 2
    size //= 2

checksum = ''
for i in range(size):
    to_eval = inp[i * ans: (i+1) * ans]
    checksum += '0' if to_eval.count('1') % 2 else '1'

print(checksum)
