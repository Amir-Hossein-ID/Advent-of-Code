st = 'abcdefgh'

for i in range(100): # no of lines of input
    s = input().split()
    if s[0] == 'swap':
        if s[1] == 'position':
            st1 = list(st)
            st1[int(s[2])], st1[int(s[5])] = st1[int(s[5])], st1[int(s[2])]
            st = "".join(st1)
        else:
            st = st.translate(str.maketrans(s[2]+s[5], s[5]+s[2]))
    elif s[0] == 'rotate':
        if s[1] == 'right':
            torot = int(s[2]) % len(st)
            st = st[-torot:] + st[:-torot]
        elif s[1] == 'left':
            torot = int(s[2]) % len(st)
            st = st[torot:] + st[:torot]
        else:
            torot = st.index(s[-1])
            torot += 1 if torot < 4 else 2
            torot %= len(st)
            st = st[-torot:] + st[:-torot]
    elif s[0] == 'reverse':
        st1 = list(st)
        st1[int(s[2]):int(s[4])+1] = st1[int(s[2]):int(s[4])+1][::-1]
        st = ''.join(st1)
    else:
        st1 = list(st)
        a = st1.pop(int(s[2]))
        st1.insert(int(s[-1]), a)
        st = ''.join(st1)

print(st)
