reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

commands = []

for i in range(23): # no of lines of input
    commands.append(input().split())

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

    i += 1

print(reg['a'])
