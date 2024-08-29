disk_round = []
disk_pos = []

for i in range(6): # no of lines of input
    s = input().split()
    disk_round.append(int(s[3]))
    disk_pos.append((int(s[-1][:-1]) + i + 1) % disk_round[-1])

sorted_i = sorted(range(len(disk_round)), key=lambda x: disk_round[i], reverse=True)

added = 0

while any(disk_pos):
    for i in sorted_i:
        to_add = disk_pos[i] % disk_round[i]
        if to_add:
            to_add = disk_round[i] - to_add
            added += to_add
            disk_pos = [(disk_pos[j] + to_add) % disk_round[j] for j in range(len(disk_pos))]
            break

print(added)
