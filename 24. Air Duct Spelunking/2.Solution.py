from heapq import heappop, heappush
from collections import deque

table = []
orig = 0
points = []
for i in range(37): # no of lines of input
    s = input()
    for j in range(len(s)):
        if s[j] == '0':
            orig = (i, j)
        elif s[j] != '#' and s[j] != '.':
            points.append((i, j))
    table.append(s)

def dis(orig, dest):
    a = [(0, orig)]
    visited = set()
    while a:
        distance, cur = heappop(a)
        if cur == dest:
            return distance
        for i, j in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            newpoint = (cur[0] + i, cur[1] + j)
            if newpoint in visited:
                continue
            if table[newpoint[0]][newpoint[1]] == '#':
                continue
            visited.add(newpoint)
            heappush(a, (distance + 1, newpoint))

points.insert(0, orig)
dises = [[0] * len(points) for i in range(len(points))]
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = dis(points[i], points[j])
        dises[i][j] = distance
        dises[j][i] = distance

queue = deque()
queue.append(({0}, 0, 0)) # visited, cost, last
ans = float('inf')
a = set()
while queue:
    visited, cost, last = queue.popleft()
    if len(visited) == len(dises):
        ans = min(ans, cost + dises[last][0])
        continue
    for i in range(len(dises)):
        if i not in visited:
            queue.append((visited.union({i}), cost + dises[last][i], i))

print(ans)
