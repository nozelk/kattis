from math import floor

commission = 0.03
cadin = 1000.0
usdin = 0
exrate = []

usd = [0] * 366
cad = [0] * 366

cad[0] = cadin


while True:
    dnevi = int(input())
    if dnevi == 0:
        break

    for i in range(dnevi):
           tmp = float(input())
           exrate.append(tmp)

    for i in range(dnevi):
                        #kaj ce nebi sploh se prej spreminjali,      trenutn    ce spreminjamo sedaj naprej
        cad[i + 1] = max(floor(cadin + usdin * exrate[i] * (1 - commission) * 100) / 100, cad[i], floor(usd[i] * exrate[i] * (1 - commission) * 100) / 100)
        usd[i + 1] = max(floor(usdin + cadin / exrate[i] * (1 - commission) * 100) / 100, usd[i], floor(cad[i] / exrate[i] * (1 - commission) * 100) / 100)
    
    print(f"%.2f" % cad[dnevi])

    exrate = []