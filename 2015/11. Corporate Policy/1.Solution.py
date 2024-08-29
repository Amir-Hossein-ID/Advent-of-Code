p = list(input())

def incr(pas):
    curr = len(pas) - 1
    while True:
        pas[curr] = chr((ord(pas[curr]) - 97 + 1)%26 + 97)
        if pas[curr] == 'a':
            curr -= 1
        elif pas[curr] == 'i' or pas[curr] == 'o' or pas[curr] == 'l':
            pas[curr] = chr((ord(pas[curr]) - 97 + 1)%26 + 97)
            pas[curr+1:] = ['a' for i in range(len(pas) - curr - 1)]
            curr = len(pas) - 1
        else:
            break

def check(pas):
    last2 = 0
    last1 = 0
    p = [ord(i) for i in pas]
    for i in p:
        if i in [105, 108, 111]: # i l o
            return False
        if i == last1 + 1 and last1 == last2 + 1:
            break
        last2 = last1
        last1 = i
    else:
        return False
    t = 0
    i = 1
    while i < len(p):
        if p[i] == p[i-1]:
            t += 1
            i += 1
        i += 1
    return t >= 2

incr(p)
while not check(p):
    incr(p)
print("".join(p))
