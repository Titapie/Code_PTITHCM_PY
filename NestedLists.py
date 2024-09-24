n=int(input())
a=[]
for i in range(0,n):
    s=input()
    k=float(input())
    a.insert(len(a),list([s,k]))

for i in range(0,n):
    for j in range(i,n):
        if a[i][1]>a[j][1]: a[i],a[j]=a[j],a[i]

b=[]
for i in range(1,n):
    if a[0][1]!=a[i][1] :
     
        if a[i-1][1]!=a[0][1] and a[i][1]!=a[i-1][1] and i-1 !=0 :break
        b.insert(len(b),a[i][0])
        
b.sort()
for i in b:
    print(i)
