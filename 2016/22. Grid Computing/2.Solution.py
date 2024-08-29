width = 37
height = 27

input()
input()
data = [[0] * width for _ in range(height)] # no of input
for j in range(width): #no of lines of input
    for i in range(height):
        s = input().split()
        data[i][j] = [int(p[:-1]) for p in s[1:]]

freespot_x = -1
freespot_y = -1

# for i in range(height):
#     for j in range(width):
#         if data[i][j][1] == 0:
#             print('_', end=' ')
#         elif data[i][j][0] < 100:
#             print('.', end=' ')
#         else:
#             print('#', end=' ')
#     print('')

for i in range(height):
    for j in range(width):
        if data[i][j][1] == 0:
            freespot_y = i
            freespot_x = j
            break
    else:
        continue
    break

ans = 0

while freespot_y != 0:
    if data[freespot_y-1][freespot_x][1] < 100:
        freespot_y -= 1
    else:
        freespot_x -= 1
    ans += 1

ans += width - 2 - freespot_x

# now for goal to move to left 5 step is required:
# . _ G   ---   . G _   ---   . G .   ---   . G .   ---   . G .   ---   _ G .
# . . .   ---   . . .   ---   . . _   ---   . _ .   ---   _ . .   ---   . . .

ans += (width - 2) * 5 + 1

print(ans)
