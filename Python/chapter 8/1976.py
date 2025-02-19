n = int(input())
m = int(input())
dosi = [[0 for _ in range(n+1)]for _ in range(n+1)]

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[b] = a

for i in range(1, n+1):
    dosi[i] = list(map(int, input().split()))
    dosi[i].insert(0,0)

route = list(map(int, input().split()))
route.insert(0,0)

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    for j in range(1, n+1):
        if dosi[i][j] == 1:
            union(i,j)

index = find(route[1])
isConnect = True
for i in range(2, len(route)):
    if index != find(route[i]):
        isConnect = False
        break

if isConnect:
    print("YES")
else:
    print("NO")