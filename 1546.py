t =int(input())
s=list(map(int,input().split()))
max_s=max(s)
for i in range(t):
    s[i]=s[i]/(max_s)*100
print("%.2f" %(sum(s)/ t))
