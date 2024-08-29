inp = input()
disk = 272

while len(inp) < disk:
    inp = inp + '0' + inp[::-1].translate(str.maketrans('01', '10'))

inp = inp[:disk]
checksum = inp

while len(checksum) % 2 == 0:
    newcheck = ''
    for i in range(0, len(checksum), 2):
        if checksum[i] == checksum[i+1]:
            newcheck += '1'
        else:
            newcheck += '0'
    checksum = newcheck

print(checksum)
