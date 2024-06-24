from collections import deque

n = int(input())

lefts = deque(range(1, n//2+1))
rights = deque(range(n//2+1, n+1))

while rights:
    if len(lefts) > len(rights):
        lefts.pop()
    else:
        rights.popleft()
    if not rights:
        break
    lefts.append(rights.popleft())
    rights.append(lefts.popleft())

print(lefts.pop())
