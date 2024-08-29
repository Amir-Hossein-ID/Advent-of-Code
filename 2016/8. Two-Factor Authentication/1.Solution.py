rows = 6
cols = 50
my = [[False for i in range(cols)] for i in range(rows)]

for i in range(153): # no of lines of input
    s = input().split()
    if s[0] == 'rect':
        a,b = [int(i) for i in s[1].split('x')]
        for i in range(b):
            for j in range(a):
                my[i][j] = True
    elif s[1] == 'row':
        row = int(s[2][2:])
        shift = int(s[4]) % cols
        my[row] = my[row][cols - shift:] + my[row][:cols - shift]
    else:
        col = int(s[2][2:])
        shift = int(s[4]) % rows
        newcol = [my[i - shift][col] for i in range(rows)]
        for i in range(rows):
            my[i][col] = newcol[i]

print(sum(sum(i) for i in my))
