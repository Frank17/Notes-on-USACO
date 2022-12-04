import sys
from bisect import insort

lines = sys.stdin.readlines()[1:]
cows = [[*map(int, line.split())] for line in lines]
cows.sort()

rqed_bk_n = avai_bk_n = 0
is_milking = []

for si, ti, bi in cows:
	while is_milking:
		tj, bj = is_milking[-1]
		if tj >= si:    # this cow is still milking
			break
		avai_bk_n += bj
		is_milking.pop()
	
	free_bk_n = min(avai_bk_n, bi)
	avai_bk_n -= free_bk_n
	rqed_bk_n += (bi - free_bk_n)
	insort(is_milking, (ti, bi), key=lambda c: -c[0])

	
print(rqed_bk_n)
