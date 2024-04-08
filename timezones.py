time_zones = {
    "UTC": 0,
    "GMT": 0, "BST": 1, "IST": 1, "WET": 0, "WEST": 1,
    "CET": 1, "CEST": 2, "EET": 2, "EEST": 3, "MSK": 3, "MSD": 4,
    "AST": -4, "ADT": -3, "NST": -3.5, "NDT": -2.5, "EST": -5,
    "EDT": -4, "CST": -6, "CDT": -5, "MST": -7, "MDT": -6,
    "PST": -8, "PDT": -7, "HST": -10, "AKST": -9, "AKDT": -8,
    "AEST": 10, "AEDT": 11, "ACST": 9.5, "ACDT": 10.5, "AWST": 8
}

#with open("moje_res.txt","w",encoding="utf-8") as dat:
N = int(input())
for i in range(N):
    vrstica = input().split(" ")
    if vrstica[0] == "noon":
        s_c = 12 * 60
        iz_katerega = vrstica[1]
        v_katerega = vrstica[2]
    elif vrstica[0] == "midnight":
        s_c = 0
        iz_katerega = vrstica[1]
        v_katerega = vrstica[2]
    else:
        ura, minuta = map(int, vrstica[0].split(":"))
        s_c = ura * 60 + minuta
        if vrstica[1] == "a.m." and ura == 12:
            s_c = minuta
        elif ura < 12 and vrstica[1] == "p.m.":
            s_c += 12 * 60
        iz_katerega = vrstica[2]
        v_katerega = vrstica[3]
    razilka = (time_zones[v_katerega]  - time_zones[iz_katerega]) * 60
    s_c += razilka
    cas = (s_c + 24*60) % (24*60)
    if cas == 0:
        print("midnight")
        continue
    elif cas == 12 * 60:
        print("noon")
        continue
    ura = cas // 60
    minuta = cas % 60
    if ura == 0:
        ura = 12
        a_p = "a.m."
    elif ura < 12:
        a_p = "a.m."
    elif ura == 12:
        a_p = "p.m."
    else:
        ura -= 12
        a_p = "p.m."
    print(f"{int(ura)}:{int(minuta):02} {a_p}")