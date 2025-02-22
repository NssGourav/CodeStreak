def dragon(s, dragons):
    dragons.sort()  
    for i, j in dragons:
        if s > i:
            s += j  
        else:
            return "NO" 
    return "YES" 
s, n = map(int, input().split())
dragons = []

for _ in range(n):
    i, j = map(int, input().split())
    dragons.append((i, j))  
print(dragon(s, dragons))  
