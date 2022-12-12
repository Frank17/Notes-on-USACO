import sys

inp = sys.stdin.readline
n = int(inp())
petals = [int(p) for p in inp().split()]
avg_pics_n = n

for i in range(n):
    for j in range(i + 1, n):
        pic = petals[i : j + 1]
        avg = sum(pic) / (j - i)
        if avg in pic:
            avg_pics_n += 1

print(avg_pics_n)
