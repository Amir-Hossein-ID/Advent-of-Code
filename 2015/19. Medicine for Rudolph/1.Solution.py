trans = {}

s = input()
while s:
    a, b = s.split(' => ')
    if a in trans:
        trans[a].append(b)
    else:
        trans[a] = [b]
    s = input()

mol = input()

all = set()

for i in trans:
    fr = 0
    ind = mol.find(i, fr)
    while ind != -1:
        for j in trans[i]:
            all.add(mol[:fr] + mol[fr:].replace(i, j, 1))
        fr = ind + 1
        ind = mol.find(i, fr)

print(len(all))
