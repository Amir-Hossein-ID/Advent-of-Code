reg = {'a': 7, 'b': 0, 'c': 0, 'd': 0}

commands = []

for i in range(26): # no of lines of input
    commands.append(input().split())

i = 0

while i < len(commands) and i > -1:
    cur = commands[i]
    if cur[0] == 'inc':
        reg[cur[1]] += 1
    elif cur[0] == 'dec':
        reg[cur[1]] -= 1
    elif cur[0] == 'cpy':
        reg[cur[2]] = int(reg.get(cur[1], cur[1]))
    elif cur[0] == 'jnz':
        if cur[1] in reg:
            if reg[cur[1]] != 0:
                i += int(reg.get(cur[2], cur[2]))
                continue
        elif int(cur[1]) != 0:
            i += int(reg.get(cur[2], cur[2]))
            continue
    elif cur[0] == 'tgl':
        toch = i + int(reg.get(cur[1], cur[1]))
        if toch < len(commands):
            newcom = commands[toch]
            if len(newcom) == 2:
                if newcom[0] == 'inc':
                    commands[toch][0] = 'dec'
                else:
                    commands[toch][0] = 'inc'
            else:
                if newcom[0] == 'jnz':
                    commands[toch][0] = 'cpy'
                else:
                    commands[toch][0] = 'jnz'
    i += 1

print(reg['a'])
