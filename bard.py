import sys

število_pesmi = 0
pozna = [[0 for j in range(50)] for i in range(101)]

input_lines = sys.stdin.readlines()

N = int(input_lines[0])
V = int(input_lines[1])

for line in input_lines[2:]:
    vecer = int(line.split()[0])
    prisotni = [0] * (N+1)
    pojejo = [0] * 50

    for i in range(1, vecer+1):
        kdo = int(line.split()[i])
        prisotni[kdo] = 1

    if prisotni[1]:
        pojejo[število_pesmi] = 1
        število_pesmi += 1
    else:
        for j in range(število_pesmi):
            for k in range(1, N+1):
                if prisotni[k] and pozna[k][j]:
                    pojejo[j] = 1

    for k in range(1, N+1):
        for j in range(število_pesmi):
            if prisotni[k] and pojejo[j]:
                pozna[k][j] = 1

for i in range(1, N+1):
    pozna_vse = all(pozna[i][j] for j in range(število_pesmi))
    if pozna_vse:
        print(i)
