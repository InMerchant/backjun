a, b, c = map(int, input().split())

if(a==b==c):
    award = 10000+a*1000
elif(a==b):
    award = 1000+a*100
elif(a==c):
    award = 1000+a*100
elif(b==c):
    award = 1000+b*100
else:
    award = max(a,b,c)*100

print(award)