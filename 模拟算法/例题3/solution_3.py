import sys
from heapq import heappop, heappush

lines = sys.stdin.readlines()[1:]
milk_info = [[*map(int, line.split())] for line in lines]
milk_info.sort()

rqed_bk_n = avai_bk_n = 0
is_milking = []

for si, ti, bi in milk_info:
	while is_milking:
		tj, bj = is_milking[0]
		if tj >= si:    # this cow is still milking
			break
		avai_bk_n += bj
		heappop(is_milking)

	free_bk_n = min(avai_bk_n, bi)
	avai_bk_n -= free_bk_n
	rqed_bk_n += (bi - free_bk_n)
	heappush(is_milking, (ti, bi))
	
print(rqed_bk_n)
