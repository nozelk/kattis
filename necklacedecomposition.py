def necklace(T):
    n = len(T)
    for i in range(1, n):
        for j in range(n):
            if T[j] < T[(i+j) % n]:
                break
            if T[j] > T[(i+j) % n]:
                return False
    return True

def decomp(S):
    D = []
    i = 0
    while i < len(S):
        t = ""
        while i < len(S) and S[i] == '0':
            t += '0'
            i += 1
        while i < len(S) and S[i] == '1':
            t += '1'
            i += 1
        D.append(t)

    changed = True
    while changed:
        newD = []
        changed = False
        j = 0
        while j < len(D):
            if j < len(D) - 1 and D[j] <= D[j+1]:
                changed = True
                newD.append(D[j] + D[j+1])
                j += 2
            else:
                newD.append(D[j])
                j += 1

        if not changed:
            D = newD
            newD = []
            j = 0
            while j < len(D):
                if j < len(D) - 1 and necklace(D[j] + D[j+1]):
                    changed = True
                    newD.append(D[j] + D[j+1])
                    j += 2
                else:
                    newD.append(D[j])
                    j += 1

        D = newD

    for item in D:
        print(f"({item})", end="")

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        S = input()
        decomp(S)
        print()
