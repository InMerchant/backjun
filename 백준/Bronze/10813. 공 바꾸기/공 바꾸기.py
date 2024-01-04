# N은 바구니 개수 M은 공을 바꾸는 횟 수
N, M = map(int, input().split())
list = [0]*N

for a in range(N):
    list[a] = a+1


for b in range(M):
    i, j = map(int, input().split())
    temp = list[i-1]
    list[i-1] = list[j-1]
    list[j-1] = temp
    
for c in range(len(list)):
    print(list[c], end=" ")