N = int(input())

    
for i in range(N):
    print(" "*(N-i-1) + "*"*((i+1)*2-1))
for j in range(N, 0, -1):
    print(" "*(N-j+1) + "*"*((j-1)*2-1))