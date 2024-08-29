import math
import itertools

hit, damage, armor = [int(input().split()[-1]) for _ in range(3)]

weapons = [
    {"cost": 8, "damage": 4, "armor": 0},
    {"cost": 10, "damage": 5, "armor": 0},
    {"cost": 25, "damage": 6, "armor": 0},
    {"cost": 40, "damage": 7, "armor": 0},
    {"cost": 74, "damage": 8, "armor": 0}
]

armors = [
    {"cost": 0, "damage": 0, "armor": 0},
    {"cost": 13, "damage": 0, "armor": 1},
    {"cost": 31, "damage": 0, "armor": 2},
    {"cost": 53, "damage": 0, "armor": 3},
    {"cost": 75, "damage": 0, "armor": 4},
    {"cost": 102, "damage": 0, "armor": 5}
]

rings = [
    {"cost": 0, "damage": 0, "armor": 0},
    {"cost": 25, "damage": 1, "armor": 0},
    {"cost": 50, "damage": 2, "armor": 0},
    {"cost": 100, "damage": 3, "armor": 0},
    {"cost": 20, "damage": 0, "armor": 1},
    {"cost": 40, "damage": 0, "armor": 2},
    {"cost": 80, "damage": 0, "armor": 3}
]


my_armor = 0
my_hit = 100
my_damage = 0

min_cost = -1

for wep, arm, ring1, ring2 in itertools.product(weapons, armors, rings, rings):
    if ring1 == ring2 and ring1 != rings[0]:
        continue
    my_armor = arm['armor'] + ring1['armor'] + ring2['armor']
    my_damage = wep['damage'] + ring1['damage'] + ring2['damage']

    cost = arm['cost'] + wep['cost'] + ring1['cost'] + ring2['cost']
    
    my_damage = max(my_damage - armor, 1)
    his_damage = max(damage - my_armor, 1)

    if math.ceil(hit / my_damage) > math.ceil(my_hit / his_damage):
        continue

    if min_cost > cost or min_cost == -1:
        min_cost = cost
        

print(min_cost)
