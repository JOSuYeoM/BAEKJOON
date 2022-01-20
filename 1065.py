n = int(input())
num = set()
for i in range(1,n+1):
    if i < 100:
        num.add(i)
    elif i < 1000:
        if (((i//100)-((i//10)%10)) == (((i//10)%10)-(i%10))) :
            num.add(i)
print(len(num))