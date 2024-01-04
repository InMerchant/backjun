N = int(input())
L = list(map(int, input().split()))

m = max(L)
sum = 0
for i in range(len(L)):
    L[i] = L[i]/m*100

for j in range(len(L)):
    sum = sum+L[j]
print(sum/len(L))