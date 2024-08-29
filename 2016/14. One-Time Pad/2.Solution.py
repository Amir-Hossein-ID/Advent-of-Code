from hashlib import md5

s = input()
num = 0
hashes = dict()
keys = []

def get_hash(st):
    return md5(st.encode()).hexdigest().lower()

def get2016hash(st):
    if st in hashes:
        return hashes[st]
    st1 = st
    for i in range(2017):
        st = get_hash(st)
    hashes[st1] = st
    return st

def has3(st):
    for i in range(len(st)-2):
        if st[i] == st[i+1] == st[i+2]:
            return st[i]
    return None

while len(keys) != 64:
    hash_ = get2016hash(s + str(num))
    if e:=has3(hash_):
        for i in range(1, 1001):
            if e*5 in get2016hash(s + str(num + i)):
                keys.append(num)
                # print(num)
                break
    num += 1

print(keys[-1])
