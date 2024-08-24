
commands = []

for i in range(30): # no of lines of input
    commands.append(input().split())


def run_commands(commands, a_default):
    reg = {'a': a_default, 'b': 0, 'c': 0, 'd': 0}

    i = 0

    while i < len(commands) and i > -1:
        cur = commands[i]
        if cur[0] == 'inc':
            reg[cur[1]] += 1
        elif cur[0] == 'dec':
            reg[cur[1]] -= 1
        elif cur[0] == 'cpy':
            if cur[1] in reg:
                reg[cur[2]] = reg[cur[1]]
            else:
                reg[cur[2]] = int(cur[1])
        elif cur[0] == 'jnz':
            if cur[1] in reg:
                if reg[cur[1]] != 0:
                    i += int(cur[2])
                    continue
            elif int(cur[1]) != 0:
                i += int(cur[2])
                continue
        elif cur[0] == 'out':
            yield int(reg.get(cur[1], cur[1]))

        i += 1
    return reg

a = 1
req = [1 if i%2 else 0 for i in range(8)]
while True:
    b = 8
    new = []
    for i in run_commands(commands, a):
        new.append(i)
        b -= 1
        if not b:
            break
    if req == new:
        print(a)
        break
    a += 1
