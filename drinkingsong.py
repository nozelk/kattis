def bottles_of_beer(n, beverage):
    lyrics = []
    for i in range(n, 0, -1):
        if i == 1:
            lyrics.append(f"{i} bottle of {beverage} on the wall, {i} bottle of {beverage}.")
            lyrics.append(f"Take it down, pass it around, no more bottles of {beverage}.")
        elif i == 2:
            lyrics.append(f"{i} bottles of {beverage} on the wall, {i} bottles of {beverage}.")
            lyrics.append(f"Take one down, pass it around, {i-1} bottle of {beverage} on the wall.")
        else:
            lyrics.append(f"{i} bottles of {beverage} on the wall, {i} bottles of {beverage}.")
            lyrics.append(f"Take one down, pass it around, {i-1} bottles of {beverage} on the wall.")
        lyrics.append("")
    return "\n".join(lyrics)

# Branje vhodnih podatkov
n = int(input())
beverage = input().strip()

# Generiranje besedila pesmi
besedilo_pesmi = bottles_of_beer(n, beverage)

# Izpis besedila pesmi
print(besedilo_pesmi,end="")