import sys

R, C, Vertical, Horizontal = map(int, input().split())

in_ = [list(input()) for i in range(R)]

for i in range(R * Vertical):
    row = i // Vertical
    for j in range(C * Horizontal):
        col = j // Horizontal
        sys.stdout.write(in_[row][col])
    sys.stdout.write('\n')
