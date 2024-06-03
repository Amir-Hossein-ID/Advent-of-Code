from queue import PriorityQueue

trans = []

s = input()
while s:
    a, b = s.split(' => ')
    trans.append((b,a))
    s = input()
trans = sorted(trans, key=lambda x:len(x[0]), reverse=True)

mol = input()

all = PriorityQueue()
all.put((len(mol), mol))
steps = {mol: 0}

while True:
    _, inp = all.get()
    for i,j in trans:
        ind = inp.find(i)
        if ind != -1:
            new = inp.replace(i, j, 1)
            new_steps = steps.get(new, steps[inp] + 1)
            steps[new] = new_steps
            all.put((len(new), new))
            if new == 'e':
                print(new_steps)
                exit()
