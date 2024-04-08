N, C = map(int, input().split())
W = [0] + list(map(int, input().split()))
s = e = i = 1
vsotaW = W[i]
start = [0] * (N + 1)
end = [0] * (N + 1)
while s <= N:
    
    if e + 1 > N or vsotaW + W[e + 1] > C:
        end[s] = i
        vsotaW -= W[s]
        s += 1
        
    else:
        e += 1
        start[e] = i
        vsotaW += W[e]
    i += 1
        
#print(end,start)
print(*[end[x] - start[x] for x in range(1, N + 1)], sep="\n")