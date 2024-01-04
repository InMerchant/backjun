e = [1, 1, 2, 2, 2, 8]

q = list(map(int, input().split()))

for i in range(len(e)):
    e[i] = e[i] - q[i]

for j in range(6):
    print(e[j],end=" ")