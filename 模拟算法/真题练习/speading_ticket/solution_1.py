import sys

lines = [[*map(int, line.split())] for line in sys.stdin.readlines()]
road_seg_n = lines[0][0]

road_segs = lines[1: road_seg_n + 1]
road_total_lmts = []
for r_len, r_lmt in road_segs:
	road_total_lmts += [r_lmt] * r_len

cow_segs = lines[road_seg_n + 1:]
cow_total_spds = []
for c_len, c_spd in cow_segs:
	cow_total_spds += [c_spd] * c_len
  
max_overspd = 0
for r_lmt, c_spd in zip(road_total_lmts, cow_total_spds):
	max_overspd = max(max_overspd, c_spd - r_lmt)

print(max_overspd)
