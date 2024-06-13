from queue import Queue
from copy import deepcopy

floors = []

for i in range(4): # no of levels
    s = input().strip('.').split(',')
    if len(s) == 1:
            s = s[0].split(' and')
    floor = list()
    for j in s:
        ss = j.split()
        if ss[-1] == 'generator':
            floor.append(('g', ss[-2]))
        elif ss[-1] == 'microchip':
            floor.append(('m', ss[-2].split('-')[0]))
    floors.append(floor)

def check_no_fried(floors):
    for i in floors:
        chips = set()
        gens = set()
        for j in i:
            if j[0] == 'm':
                chips.add(j[1])
            else:
                gens.add(j[1])
        if gens and (chips - gens):
            return False
    return True

def unique_repr(elv, floors):
    return elv, tuple([(sum(j[0] == 'm' for j in i), sum(j[0] == 'g' for j in i)) for i in floors])

def check_move(from_level, to_level, floors, carries, moves):
    if to_level >= len(floors) or to_level < 0:
        return
    floors = deepcopy(floors)
    for i in carries[::-1]:
        floors[to_level].append(floors[from_level].pop(i))
    repr = unique_repr(to_level, floors)
    if check_no_fried(floors) and repr not in all:
        all.add(repr)
        q.put((to_level, floors, moves))

all = set()
q = Queue()
q.put((0, floors, 0))
all.add(unique_repr(0, floors))

while not q.empty():
    cur_lvl, floors, moves = q.get()

    if not any(floors[:-1]):
        print(moves)
        break

    for val1 in range(len(floors[cur_lvl])):
        for val2 in range(val1+1, len(floors[cur_lvl])):
            check_move(cur_lvl, cur_lvl + 1, floors, [val1, val2], moves + 1)
            check_move(cur_lvl, cur_lvl - 1, floors, [val1, val2], moves + 1)
        check_move(cur_lvl, cur_lvl + 1, floors, [val1], moves + 1)
        check_move(cur_lvl, cur_lvl - 1, floors, [val1], moves + 1)
