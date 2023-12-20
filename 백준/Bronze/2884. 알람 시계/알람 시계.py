a, b = map(int, input().split())

if(b >= 45):
    b = b-45
elif(a==0 and b<45):
    a=a+23
    b=b+15
else:
    a = a-1
    b = b+15

print(a,b)