hit, damage = [int(input().split()[-1]) for i in range(2)]

my_hit, my_mana = 50, 500

spells = [
    {
        "mana_cost": 53,
        "name": "Magic Missile",
        "duration": 1,
        "armor_increase": 0,
        "damage_per_turn": 4,
        "mana_per_turn": 0,
        "heal": 0
    },
    {
        "mana_cost": 73,
        "name": "Drain",
        "duration": 1,
        "armor_increase": 0,
        "damage_per_turn": 2,
        "mana_per_turn": 0,
        "heal": 2
    },
    {
        "mana_cost": 173,
        "name": "Poison",
        "duration": 6,
        "armor_increase": 0,
        "damage_per_turn": 3,
        "mana_per_turn": 0,
        "heal": 0
    },
    {
        "mana_cost": 229,
        "name": "Recharge",
        "duration": 5,
        "armor_increase": 0,
        "damage_per_turn": 0,
        "mana_per_turn": 101,
        "heal": 0
    },
    {
        "mana_cost": 113,
        "name": "Shield",
        "duration": 6,
        "armor_increase": 7,
        "damage_per_turn": 0,
        "mana_per_turn": 0,
        "heal": 0
    },
]

min_found = float('inf')

def do(my_hit, enemy_hit, effects, my_mana, spent, my_turn):
    global min_found
    if spent >= min_found:
        return

    effects = [i.copy() for i in effects if i['duration'] > 0]
    arm = 0
    for i in effects:
        i['duration'] -= 1
        enemy_hit -= i['damage_per_turn']
        my_mana += i['mana_per_turn']
        my_hit += i['heal']

        arm += i['armor_increase']
    effects = [i for i in effects if i['duration'] > 0]
    if not my_turn:
        my_hit -= max(1, damage - arm)

    if enemy_hit <= 0:
        if spent < min_found:
            min_found = spent
    if my_hit <= 0:
        return
    if my_turn:
        for spell in spells:
            if my_mana >= spell['mana_cost'] and spell['name'] not in [i['name'] for i in effects]:
                do(my_hit, enemy_hit, effects + [spell],
                   my_mana - spell['mana_cost'], spent + spell['mana_cost'], False)
        
    else:
        do(my_hit, enemy_hit, effects, my_mana, spent, True)      

do(my_hit, hit, [], my_mana, 0, True)

print(min_found)
