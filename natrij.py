c1 = map(int, input().split(":"))
c2 = map(int, input().split(":"))

c1 = list(c1)
c2 = list(c2)

if c2[0] <= c1[0]:
    c2[0] += 24
    
if c2[2] < c1[2]:
    c2[2] += 60
    c2[1] -= 1

if c2[1] < c1[1]:
    c2[1] += 60
    c2[0] -= 1

ura = str(c2[0] - c1[0])
minuta = str(c2[1] - c1[1])
sekunda = str(c2[2] - c1[2])

if len(ura) != 2:
    ura = "0" + ura
    
if len(minuta) != 2:
    minuta = "0" + minuta
    
if len(sekunda) != 2:
    sekunda = "0" + sekunda
    
print(f"{ura}:{minuta}:{sekunda}")