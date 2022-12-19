import sys

board1, board2, truck = map(str.split, sys.stdin.readlines())
x11, y11, x12, y12 = map(int, board1)
x21, y21, x22, y22 = map(int, board2)
xt1, yt1, xt2, yt2 = map(int, truck)

# Get total areas
b1_total_a = (x12 - x11) * (y12 - y11)
b2_total_a = (x22 - x21) * (y22 - y21)

# Get blocked areas
get_insct_len = (lambda pb1, pb2, pt1, pt2:
    max(0, min(pb2, pt2) - max(pb1, pt1)))

b1_blocked_w = get_insct_len(x11, x12, xt1, xt2)
b1_blocked_h = get_insct_len(y11, y12, yt1, yt2)
b1_blocked_a = b1_blocked_w * b1_blocked_h

b2_blocked_w = get_insct_len(x21, x22, xt1, xt2)
b2_blocked_h = get_insct_len(y21, y22, yt1, yt2)
b2_blocked_a = b2_blocked_w * b2_blocked_h

print(b1_total_a + b2_total_a -
      b1_blocked_a - b2_blocked_a)
