import sys
from itertools import combinations

lines = sys.stdin.readlines()[1:]
ranks = [[*map(int, rank.split())] for rank in lines]
cst_pairs = set(combinations(ranks[0], 2))

for rank in ranks[1:]:
    pairs = set(combinations(rank, 2))
    cst_pairs &= pairs

print(len(cst_pairs))
