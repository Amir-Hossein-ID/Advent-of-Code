a = ""
for i in range(6):
   a += input()

s = a.find("mul(")
ans = 0

while s != -1:
    b = a.find(",", s+1)
    c = a.find(")", s+1)
    if b == -1 or c == -1:
        break
    try:
        bb = int(a[s+4:b])
        cc = int(a[b+1: c])
        
        ans += bb*cc
    except:
        pass
    finally:
        s = a.find("mul(",s+1)

print(ans)
