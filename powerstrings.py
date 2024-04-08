while True:
    s = input().strip()
    if s == ".":
        break
    
    n = len(s)  # Dolžina vhodnega niza
    lps = [0] * n  # Inicializacija seznama lps z ničlami
    length = 0  # Trenutna dolžina najdaljšega ujemanja
    i = 1  # Indeks za iteracijo skozi niz
    
    # Gradimo LPS seznam s KMP algoritmom
    while i < n:
        if s[i] == s[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    # Dolžina ponavljajočega se podniza
    repeating_length = n - lps[n - 1]
    
    # Preverimo, ali je dolžina vhodnega niza deljiva z dolžino ponavljajočega se podniza
    if n % repeating_length == 0:
        result = n // repeating_length
    else:
        result = 1
    
    print(result)
