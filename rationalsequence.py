P = int(input())

odgovori = []

for i in range(P):

    tmp = input().split()

    zap_st = int(tmp[0])
    
    stevec, imenovalec = tmp[1].split("/")
    
    stevec = int(stevec)
    imenovalec = int(imenovalec)

    if imenovalec == 1:
        odgovori.append([[1],[stevec + 1]])
    elif stevec < imenovalec:
        odgovori.append([[imenovalec],[imenovalec - stevec]])
    else:
        stopnja = stevec // imenovalec
        odgovori.append([[imenovalec],[(2 * stopnja + 1) * imenovalec - stevec]])


for ind,i in enumerate(odgovori):
    print(f"{ind + 1} {i[0][0]}/{i[1][0]}")