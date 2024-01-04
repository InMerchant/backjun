list = [i+1 for i in range(30)]
for i in range(28):
    a = int(input())
    list.remove(a)

print(min(list))
print(max(list))