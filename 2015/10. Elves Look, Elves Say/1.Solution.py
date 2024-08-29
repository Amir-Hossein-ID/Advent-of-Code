inp = input()

for i in range(40):
    new = ''
    last = inp[0]
    count = 0
    for j in inp:
        if j == last:
            count += 1
        else:
            new += str(count) + last
            count = 1
            last = j

    if count > 0:
        new += str(count) + last
    inp = new

print(len(new))
