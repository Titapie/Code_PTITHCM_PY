n=int(input())
a=[]
for i in range(0,n):
    s=input()
    k=int(input())
    a.insert(len(a),list([s,k]))
a.sort()
for i in range(0,n):
    for j in range(i,n):
        if a[i][1]>a[j][1]: a[i],a[j]=a[j],a[i]
print(a)
b=[]
for i in range(n-2,-1,-1):
    if a[n-1][1]!=a[i][1] :
        if a[i][1]!=a[i+1][1]and i+1 !=n-1 :break
        b.insert(len(b),a[i][0])
        
b.sort()
print(b)
