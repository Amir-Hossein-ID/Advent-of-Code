n = input()
where = 0
for i in range(len(n)):
    if n[i] == '(':
        where += 1
    else:
        where -= 1
    if where == -1:
        print(i+1)
        break
