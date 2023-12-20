a, b = map(int, input().split())
c = int(input())

if(b+c < 60):
    b = b+c
elif(b+c >= 60):
    temp = int((b+c)/60)
    b= (b+c)%60
    a=a+temp
    if(a>=24):
        a=a-24

print(a, b)