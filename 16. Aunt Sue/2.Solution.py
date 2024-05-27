data = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""

data = {i.split()[0]:int(i.split()[1]) for i in data.split('\n')}
ans = 0

for i in range(500): #no of lines of input
    inp = input().split(':', 1)
    sue_data = {i.split()[0]:int(i.split()[1]) for i in inp[1].strip().split(',')}
    for i in sue_data:
        if i in ['cats:', 'trees:']:
            if sue_data[i] <= data[i]:
                break
        elif i in ['pomeranians:', 'goldfish:']:
            if sue_data[i] >= data[i]:
                break
        elif sue_data[i] != data[i]:
            break
    else:
        ans = inp[0].split()[1]

print(ans)
