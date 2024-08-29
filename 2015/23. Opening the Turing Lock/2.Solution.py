reg = {'a': 1, 'b': 0}

commands = []

for i in range(48): # no of lines of input
    commands.append(input().split())

i = 0

while i < len(commands) and i > -1:
    cur = commands[i]
    if cur[0] == 'inc':
        reg[cur[1]] += 1
    elif cur[0] == 'hlf':
        reg[cur[1]] //= 2
    elif cur[0] == 'tpl':
        reg[cur[1]] *= 3
    elif cur[0] == 'jmp':
        i += int(cur[1])
        continue
    elif cur[0] == 'jie':
        if reg[cur[1].strip(',')] % 2 == 0:
            i += int(cur[2])
            continue
    elif cur[0] == 'jio':
        if reg[cur[1].strip(',')] == 1:
            i += int(cur[2])
            continue
    i += 1

print(reg['b'])
