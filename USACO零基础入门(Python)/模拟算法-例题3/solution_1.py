import sys

lines = sys.stdin.readlines()[1:]
cows = [[*map(int, line.split())] for line in lines]
	
max_bk_n = 0
for i in range(1001):
    curr_bk_n = sum([bi
        for si, ti, bi in cows
        if si <= i <= ti
    ])
    max_bk_n = max(max_bk_n, curr_bk_n)

print(max_bk_n)
