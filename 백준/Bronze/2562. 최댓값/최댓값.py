list = list()
for i in range(9):
    list.insert(i,int(input()))
max = max(list)
print(max)
print(list.index(max)+1)