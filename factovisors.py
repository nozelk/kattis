import math
def resi(n, m):
    if m == 0:
        return False
    if m == 1 and n == 0:
        return True

    
    for i in range(2, int(math.sqrt(m) + 1)):
        st_trenutnih_veckratnikov = 0
        veckratnik = i
        #odstranjujemo veckratnike stevila
        while m % i == 0:
            m //= i
            st_trenutnih_veckratnikov += 1
        #nadzorujemo te veckratike stevila
        while veckratnik <= n and st_trenutnih_veckratnikov > 0:
            st_trenutnih_veckratnikov -= n // veckratnik
            veckratnik *= i
        #ce bo k vec od nic torej pomeni da ni sestavel iz toliko veckratikot tega stevila ta strevilo ne deli stega stevila
        if st_trenutnih_veckratnikov > 0:
            return False
        

    return m <= n


while True:
    try:
        n, m = map(int, input().split())
        if resi(n, m):
            print(f"{m} divides {n}!")
        else:
            print(f"{m} does not divide {n}!")
    except EOFError:
        break