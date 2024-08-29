from heapq import heappush, heappop

office = int(input())
mem = dict()

def is_wall(x, y):
    if (x, y) in mem:
        return mem[(x, y)]
    ans = x*x + 3*x + 2*x*y + y + y*y
    ans += office
    n = bin(ans).count('1')
    mem[(x, y)] = n % 2
    return n % 2

queue = [(0, (1, 1))]
reached = dict()
while queue:
    steps, cur = heappop(queue)

    if steps > 50:
        continue
    reached[cur] = min(reached.get(cur, steps), steps)
    if steps != reached[cur]:
        continue

    if cur[0] > 0 and not is_wall(cur[0] - 1, cur[1]):
        heappush(queue, (steps + 1, (cur[0] - 1, cur[1])))
    if cur[1] > 0 and not is_wall(cur[0], cur[1] - 1):
        heappush(queue, (steps + 1, (cur[0], cur[1] - 1)))
    if not is_wall(cur[0], cur[1] + 1):
        heappush(queue, (steps + 1, (cur[0], cur[1] + 1)))
    if not is_wall(cur[0] + 1, cur[1]):
        heappush(queue, (steps + 1, (cur[0] + 1, cur[1])))

print(len(reached))
