import json
import os

j = json.load(open(os.path.join(os.path.dirname(__file__), 'input.txt')))

def sumJson(js):
    ans = 0
    if isinstance(js, list):
        for i in js:
            ans += sumJson(i)
    elif isinstance(js, dict):
        for i in js:
            if js[i] == 'red':
                return 0
            ans += sumJson(js[i])
    elif isinstance(js, int):
        return js
    return ans

print(sumJson(j))
