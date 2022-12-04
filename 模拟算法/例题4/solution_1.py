import sys

board = [row.rstrip() for row in sys.stdin.readlines()]
ind_counted = set()
team_counted = set()

def get_count(seqs):
   ind_cow_n = team_cow_n = 0
   for seq in seqs:
       s = frozenset(seq)
       if len(s) == 1 and s not in ind_counted:
           ind_counted.add(s)
           ind_cow_n += 1
       if len(s) == 2 and s not in team_counted:
           team_counted.add(s)
           team_cow_n += 1
   return ind_cow_n, team_cow_n


r_diag = board[0][0] + board[1][1] + board[2][2]
l_diag = board[0][2] + board[1][1] + board[2][0]
cow_n = [get_count(board),              # Check rows
         get_count(zip(*board)),        # Check columns
         get_count([r_diag, l_diag])]   # Check diagonals

ind_n, team_n = map(sum, zip(*cow_n))
print(ind_n)
print(team_n)
