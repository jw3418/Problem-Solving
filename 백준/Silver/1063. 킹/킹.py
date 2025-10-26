import sys
input = sys.stdin.readline

K, S, N = input().split(); N = int(N)
king_pos = [8 - int(K[1]), ord(K[0]) - ord('A')]
stone_pos = [8 - int(S[1]), ord(S[0]) - ord('A')]

D = dict()
D['R'] = (0, 1); D['L'] = (0, -1); D['B'] = (1, 0); D['T'] = (-1, 0)
D['RT'] = (-1, 1); D['LT'] = (-1, -1); D['RB'] = (1, 1); D['LB'] = (1, -1)

for _ in range(N):
    direction = input().strip()
    dx, dy = D[direction]
    if 0 <= king_pos[0] + dx < 8 and 0 <= king_pos[1] + dy < 8:
        king_pos[0] += dx
        king_pos[1] += dy
    if king_pos == stone_pos:
        if 0 <= stone_pos[0] + dx < 8 and 0 <= stone_pos[1] + dy < 8:
            stone_pos[0] += dx
            stone_pos[1] += dy
        else:
            king_pos[0] -= dx
            king_pos[1] -= dy
print(chr(king_pos[1] + ord('A')) + str(8 - king_pos[0]))
print(chr(stone_pos[1] + ord('A')) + str(8 - stone_pos[0]))