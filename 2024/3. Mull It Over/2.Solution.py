a = ""
for i in range(6):
   a += input()

s = a.find("mul(")
do = a.find("do()")
dont = a.find("don't()")
can = True

ans = 0
while s != -1:
    if do == -1:
        do = float("inf")
    if dont == -1:
        dont = float("inf")
    
    if do < s and do < dont:
        can = True
        do = a.find("do()", do+1)
    
    if dont < s and dont < do:
        can = False
        dont = a.find("don't()", dont+1)

    b = a.find(",", s+1)
    c = a.find(")", s+1)

    if b == -1 or c == -1:
        break
    try:
        bb = int(a[s+4:b])
        cc = int(a[b+1: c])
        if can: ans += bb*cc
    except:
        pass
    finally:
        s = a.find("mul(",s+1)

print(ans)
