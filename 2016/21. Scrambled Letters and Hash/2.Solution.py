st = 'fbgdceah'

todo=[]
for i in range(100):
    todo.append(input().split())
todo = todo[::-1]

for i in range(100): # no of lines of input
    s = todo[i]
    if s[0] == 'swap':
        if s[1] == 'position':
            st1 = list(st)
            st1[int(s[5])], st1[int(s[2])] = st1[int(s[2])], st1[int(s[5])]
            st = "".join(st1)
        else:
            st = st.translate(str.maketrans(s[5]+s[2], s[2]+s[5]))
    elif s[0] == 'rotate':
        if s[1] == 'right':
            torot = int(s[2]) % len(st)
            st = st[torot:] + st[:torot]
        elif s[1] == 'left':
            torot = int(s[2]) % len(st)
            st = st[-torot:] + st[:-torot]
        else:
            torot0 = st.index(s[-1])
            torot = int('70415263'[torot0]) # works only for len == 8
            torot = (torot - torot0 + len(st)) % len(st)
            st = st[-torot:] + st[:-torot]
    elif s[0] == 'reverse':
        st1 = list(st)
        st1[int(s[2]):int(s[4])+1] = st1[int(s[2]):int(s[4])+1][::-1]
        st = ''.join(st1)
    else:
        st1 = list(st)
        a = st1.pop(int(s[-1]))
        st1.insert(int(s[2]), a)
        st = ''.join(st1)

print(st)
