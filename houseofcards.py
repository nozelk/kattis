h = int(input())

while (3 * h**2 + h) // 2 % 4 != 0:
    h += 1

print(h)
