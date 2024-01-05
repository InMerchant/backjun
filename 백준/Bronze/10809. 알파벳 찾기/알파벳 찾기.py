s = input()
al = list('abcdefghijklmnopqrstuvwxyz')
for i in range(len(al)):
    if s.count(al[i]) > 0:
        print(s.index(al[i]),end= " ")
    else :
        print("-1",end= " ")