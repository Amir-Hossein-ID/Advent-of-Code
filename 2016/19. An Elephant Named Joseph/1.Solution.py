from collections import deque
n = int(input())

q = deque(range(1, n+1))
steal = True

while q:
    last = q.popleft()
    if steal:
        q.append(last)
    steal = not steal

print(last)
