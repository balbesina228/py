n, k = int(input()), int(input())
l = [i for i in range(1, n + 1)]
while len(l) > 1:
    for _ in range(k - 1):
        l.append(l.pop(0))
    del l[0]
print(*l)
