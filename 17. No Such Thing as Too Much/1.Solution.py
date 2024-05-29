cont = [int(input()) for i in range(20)] # no of lines of input

cont.sort()

def func(target, array, fr=0):
    if target == 0:
        return 1
    c = 0
    for i,j in enumerate(array[fr:]):
        if j <= target:
            # print(j, fr, i)
            c += func(target - j, array, fr+i+1)
    return c

print(func(150, cont))
