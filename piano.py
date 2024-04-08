MAX_DNEVI = 100  # Največje število dni v tednu
class TedenIntervalov:
    def __init__(self):
        self.velikost = MAX_DNEVI
        self.povezave = [[0] * MAX_DNEVI for _ in range(MAX_DNEVI)]  # Matrika za shranjevanje povezav med intervali
        self.intervali = [[0] * MAX_DNEVI for _ in range(MAX_DNEVI)]  # Matrika za shranjevanje intervalov

def pobrisi_povezave(teden):
    teden.povezave = [[0] * MAX_DNEVI for _ in range(MAX_DNEVI)]  # Ponastavi povezave na 0
    teden.intervali = [[0] * MAX_DNEVI for _ in range(MAX_DNEVI)]  # Ponastavi intervale na 0

def seštej_intervali(teden):
    
    for i in range(teden.velikost):
        #vsota = teden.intervali[i][i]  # Vsoto intervalov na dan i postavimo na vrednost tega dneva
        vsota = 0
        #print(vsota)
        for j in range(i - 1, -1, -1):
            vsota += teden.intervali[j][i]  # Dodamo intervali prejšnjih dni
            teden.intervali[j][i] = vsota  # Posodobimo matriko intervalov

def izracunaj_povezave(teden):
    for i in range(teden.velikost):
        teden.povezave[i][i] = teden.intervali[i][i]  # Povezave na samem sebi so enake intervalom
    for i in range(1, teden.velikost):
        for j in range(teden.velikost - i):
            teden.povezave[j][j + i] = teden.povezave[j][j + i - 1] + teden.intervali[j][j + i]  # Izračun povezav

def resi_intervali(tedni, p):
    vikend = False  # Zastavica za preverjanje vikenda
    for i in range(tedni.velikost):
        delovni_dnevi = 0  # Števec delovnih dni
        for j in range(i, -1, -1):
            delovni_dnevi += (j % 7) < 5  # Preverimo, ali je dan delovni dan (pon-pet)
            if delovni_dnevi * p < tedni.povezave[j][i]:
                vikend = True  # Če ni dovolj pianistov za premike, označimo vikend
                if (i - j + 1) * p < tedni.povezave[j][i]:
                    return "serious trouble"  # Če ni mogoče izvesti premikov, vrnemo "serious trouble"
    if vikend:
        return "weekend work"  # Če morata vsaj dva pianista delati vikend, vrnemo "weekend work"
    else:
        return "fine"  # Vse ostale primere označimo kot "fine"

if __name__ == "__main__":
    Tedni = TedenIntervalov()  # Ustvarimo objekt TedenIntervalov
    n = int(input())  # Preberemo število testnih primerov
    for _ in range(n):
        pobrisi_povezave(Tedni)  # Ponastavimo povezave in intervale
        m, p = map(int, input().split())  # Preberemo število klavirjev in pianistov
        p = p // 2  # Delimo število pianistov s 2, saj delajo v parih
        for _ in range(m):
            zacetek, konec = map(int, input().split())  # Preberemo naročila za premik klavirjev
            Tedni.intervali[zacetek - 1][konec - 1] += 1  # Povečamo ustrezne vrednosti v matriki intervalov
        #print(Tedni.intervali)
        seštej_intervali(Tedni)  # Izračunamo seštevek intervalov
        #print("Po sestej",Tedni.intervali)
        izracunaj_povezave(Tedni)  # Izračunamo povezave med intervali
        #print("Po povezave",Tedni.povezave)
        rezultat = resi_intervali(Tedni, p)  # Rešimo tedenski interval in dobimo rezultat
        print(rezultat)  # Izpišemo rezultat za trenutni testni primer
