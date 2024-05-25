from itertools import permutations

happ = {'___': {}}

for i in range(56): # no of lines of input
    inp = input().strip('.').split()
    if inp[0] in happ:
        happ[inp[0]][inp[-1]] = -int(inp[3]) if inp[2] == 'lose' else int(inp[3])
    else:
        happ[inp[0]] = {inp[-1]: -int(inp[3]) if inp[2] == 'lose' else int(inp[3]), '___': 0} # my name is ___
        happ['___'][inp[0]] = 0

new_happ = {}

for i in happ:
    for j in happ[i]:
        new_happ[(i, j)] = happ[i][j] + happ[j][i]

total_ans = None

for i in permutations(happ):
    local_ans = 0
    for j in range(len(i)-1):
        local_ans += new_happ[(i[j], i[j+1])]
    local_ans += new_happ[(i[0], i[-1])]
    if total_ans == None or local_ans > total_ans:
        total_ans = local_ans

print(total_ans)
