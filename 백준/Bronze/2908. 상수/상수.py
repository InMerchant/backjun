a, b = input().split()
c = int(a[::-1])
d = int(b[::-1])
print(c) if c > d else print(d)