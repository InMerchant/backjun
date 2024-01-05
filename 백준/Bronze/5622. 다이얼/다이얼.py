X = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

S = input()

sum = 0
for i in range(len(S)):
    for j in X:
        if S[i] in j:
            sum = sum + X.index(j)+3
print(sum)