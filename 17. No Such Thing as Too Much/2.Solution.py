cont = [int(input()) for i in range(20)] # no of lines of input

cont.sort()

total = 0
min_ = 0

def func(target, array, fr=0, count=0):
    global min_, total
    if target == 0:
        if count < min_ or min_ == 0:
            min_ = count
            total = 1
        elif min_ == count:
            total += 1
        return 1
    c = 0
    for i,j in enumerate(array[fr:]):
        if j <= target:
            # print(j, fr, i)
            c += func(target - j, array, fr+i+1, count+1)
    return c
func(150, cont)
print(total)
