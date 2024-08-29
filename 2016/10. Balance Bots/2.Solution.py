from collections import defaultdict
from queue import Queue


bot_has = defaultdict(set)
bot_gives = {}
to_check = Queue()

for i in range(231): # no of lines of input
    s = input().split()
    if s[0] == 'value':
        if s[-1] in bot_has:
            to_check.put(s[-1])
        bot_has[s[-1]].add(int(s[1]))
    else:
        where = [0, 0]
        if s[5] == 'bot':
            where[0] = s[6]
        else:
            where[0] = int(s[6])
        if s[10] == 'bot':
            where[1] = s[11]
        else:
            where[1] = int(s[11])
        bot_gives[s[1]] = where

while not to_check.empty():
    cur = to_check.get()
    bot1 = bot_gives[cur][0]
    bot2 = bot_gives[cur][1]
    if bot1 != 0 and bot1 in bot_has:
        to_check.put(bot1)
    if bot2 != 0 and bot2 in bot_has:
        to_check.put(bot2)
    bot_has[bot1].add(min(bot_has[cur]))
    bot_has[bot2].add(max(bot_has[cur]))
    del bot_has[cur]

print(sum(bot_has[0]) * sum(bot_has[1]) * sum(bot_has[2]))
