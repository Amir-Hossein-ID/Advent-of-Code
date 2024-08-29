import heapq
from hashlib import md5

key = input()

tablesize = 4

queue = [(0, (1,1), '', 0)]
best_route_max = 0

while queue:
    _, cur, moves, nmoves = heapq.heappop(queue)
    if cur == (tablesize, tablesize):
        best_route_max = max(best_route_max, nmoves)
        continue
    
    doors = md5((key + moves).encode()).hexdigest()[:4]

    if cur[0] > 1 and doors[0] in 'bcdef':
        heapq.heappush(queue, (-(nmoves + 1 + (tablesize - cur[0] + 1) + (tablesize - cur[1])), (cur[0]-1, cur[1]), moves+'U', nmoves + 1))
    if cur[0] < tablesize and doors[1] in 'bcdef':
        heapq.heappush(queue, (-(nmoves + 1 + (tablesize - cur[0] - 1) + (tablesize - cur[1])), (cur[0]+1, cur[1]), moves+'D', nmoves + 1))
    if cur[1] > 1 and doors[2] in 'bcdef':
        heapq.heappush(queue, (-(nmoves + 1 + (tablesize - cur[0]) + (tablesize - cur[1] + 1)), (cur[0], cur[1]-1), moves+'L', nmoves + 1))
    if cur[1] < tablesize and doors[3] in 'bcdef':
        heapq.heappush(queue, (-(nmoves + 1 + (tablesize - cur[0]) + (tablesize - cur[1] - 1)), (cur[0], cur[1]+1), moves+'R', nmoves + 1))

print(best_route_max)
