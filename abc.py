stevilo = input()
besedilo = input()

def preveri_zaporedje(stevilo,besedilo):
    odgovor = []
    stevilo = stevilo.split()
    for i in range(len(stevilo)):
        stevilo[i] = int(stevilo[i])
    stevilo.sort()
    temp = {"A":stevilo[0], "B":stevilo[1], "C":stevilo[2]}
    for i in besedilo:
        odgovor.append(str(temp[i]))
    return odgovor[0] + " " + odgovor[1] + " " + odgovor[2]

print(preveri_zaporedje(stevilo,besedilo),end="")