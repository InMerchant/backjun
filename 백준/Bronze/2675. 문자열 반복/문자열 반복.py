T = int(input())
result = []
for i in range(T):
    R, S = input().split()
    R_int = int(R)
    for j in range(len(S)):
        result.insert(j, S[j]*R_int)
        

    for k in result:
        print(k,end="")
    result.clear()
    print(end="\n")