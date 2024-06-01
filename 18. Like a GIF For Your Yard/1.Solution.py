input_len = 100
lights = [list(input()) for _ in range(input_len)] # no of lines of input

adjastant = [[0] * input_len for _ in range(input_len)]

for _ in range(100): # no of steps
    adjastant = [[0] * input_len for _ in range(input_len)]
    for i in range(input_len):
        for j in range(input_len):
            if lights[i][j] == '#':
                if i > 0:
                    adjastant[i - 1][j] += 1
                    if j > 0:
                        adjastant[i - 1][j - 1] += 1
                    if j < input_len - 1:
                        adjastant[i - 1][j + 1] += 1
                if j > 0:
                        adjastant[i][j - 1] += 1
                if j < input_len - 1:
                        adjastant[i][j + 1] += 1
                if i < input_len - 1:
                    adjastant[i + 1][j] += 1
                    if j > 0:
                        adjastant[i + 1][j - 1] += 1
                    if j < input_len - 1:
                        adjastant[i + 1][j + 1] += 1
    for i in range(input_len):
        for j in range(input_len):
            if lights[i][j] == '#' and adjastant[i][j] not in (2,3):
                lights[i][j] = '.'
            elif lights[i][j] == '.' and adjastant[i][j] == 3:
                lights[i][j] = '#'

print(sum(sum(i == '#' for i in j) for j in lights))
