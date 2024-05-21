lights = [[0 for i in range(1000)] for i in range(1000)]

def set_lights(a, b, toggle = False, value = 0):
    for j in range(int(a[0]), int(b[0]) + 1):
            for k in range(int(a[1]), int(b[1]) + 1):
                if toggle:
                    lights[j][k] += 2
                else:
                    lights[j][k] = max(lights[j][k] + value, 0)

for i in range(300):
    ins = input().split()
    if ins[1] == 'off':
        set_lights(ins[2].split(','), ins[4].split(','), value=-1)
    elif ins[1] == 'on':
        set_lights(ins[2].split(','), ins[4].split(','), value=1)
    else:
        set_lights(ins[1].split(','), ins[3].split(','), toggle=True)

print(sum([sum(i) for i in lights]))
