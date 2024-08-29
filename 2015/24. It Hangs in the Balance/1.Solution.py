packages = []

for i in range(29): # no of lines of input
    packages.append(int(input()))

s = sum(packages) // 3

min_length = float('inf')
prod = float('inf')

def give(arr, target, level = 0):
    if level > min_length:
        return
    for i in range(len(arr)):
        if arr[i] < target:
            for j in give(arr[i+1:], target - arr[i], level + 1):
                to = [arr[i]] + j
                if len(to) <= min_length:
                    yield [arr[i]] + j
        elif arr[i] == target:
            yield [arr[i]]

for i in give(packages, s):
    if len(i) <= min_length:
        min_length = len(i)
        p = 1
        for j in i:
            p *= j
        prod = min(p, prod)

print(prod)