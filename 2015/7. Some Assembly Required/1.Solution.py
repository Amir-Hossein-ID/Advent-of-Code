values = {}
exacts = {}

def parse(inp):
    inps = inp.split()
    if inp.isdigit():
        return int(inp)
    elif inp in exacts:
        return exacts[inp]
    elif len(inps) == 1:
        a = parse(values[inp])
        exacts[inp] = a
        return a
    if 'AND' in inp:
        return parse(inps[0]) & parse(inps[2])
    if 'OR' in inp:
        return parse(inps[0]) | parse(inps[2])
    if 'LSHIFT' in inp:
        return parse(inps[0]) << parse(inps[2])
    if 'RSHIFT' in inp:
        return parse(inps[0]) >> parse(inps[2])
    if 'NOT' in inp:
        return parse(inps[1]) ^ 0xFFFF

for i in range(339): # no of lines of input
    fr, to = input().split(' -> ')
    values[to] = fr

print(parse(values['a']))
