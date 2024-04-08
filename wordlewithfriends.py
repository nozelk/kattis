def sestavi_green(beseda,testek,testirana_beseda,slovar_za_besede,slovar_za_testirane_besede):
    grin = [False] * 5
    for i in range(5):
        if beseda[i] == testirana_beseda[i]:
            testek[i] = "G"
            grin[i] = True
            slovar_za_besede[testirana_beseda[i]] -= 1
            slovar_za_testirane_besede[testirana_beseda[i]] -= 1
    return beseda,testek,testirana_beseda,slovar_za_besede,slovar_za_testirane_besede,grin

def sestavi_dokonca(testek,testirana_beseda,beseda,slovar_za_besede,slovar_za_testirane_besede,grin):
    for ind,i in enumerate(grin):
        if i:
            continue
        elif testirana_beseda[ind] in beseda and slovar_za_besede[testirana_beseda[ind]] > 0:
            testek[ind] = "Y"
            slovar_za_besede[testirana_beseda[ind]] -= 1
            slovar_za_testirane_besede[testirana_beseda[ind]] -= 1
        else:
            testek[ind] = "-"
            slovar_za_testirane_besede[testirana_beseda[ind]] -= 1
    return testek
    
def testiranje(beseda, testirana_beseda):
    testek = ["-"]*5
    slovar_za_besede = {}
    slovar_za_testirane_besede = {}

    for crka in beseda:
        if crka not in slovar_za_besede:
            slovar_za_besede[crka] = 0
        slovar_za_besede[crka] += 1

    for crka in testirana_beseda:
        if crka not in slovar_za_testirane_besede:
            slovar_za_testirane_besede[crka] = 0
        slovar_za_testirane_besede[crka] += 1

    beseda,testek,testirana_beseda,slovar_za_besede,slovar_za_testirane_besede,grin = sestavi_green(beseda,testek,testirana_beseda,slovar_za_besede,slovar_za_testirane_besede)

    testek = sestavi_dokonca(testek,testirana_beseda,beseda,slovar_za_besede,slovar_za_testirane_besede,grin)
    
    return "".join(testek)



def preveri(beseda, ugibanja):
    for testirana_beseda, test in ugibanja:
        if testiranje(beseda, testirana_beseda) != test:
            return False
    return True

testerani_besedi,koliko_besed = input().split()

testerani_besedi = int(testerani_besedi)
koliko_besed = int(koliko_besed)

ugibanja = []
for i in range(testerani_besedi):
    b, t = input().split()
    ugibanja.append((b,t))

vse_besede = []
for i in range(koliko_besed):
    vse_besede.append(input())

for beseda in vse_besede:
    if preveri(beseda,ugibanja):
        print(beseda)