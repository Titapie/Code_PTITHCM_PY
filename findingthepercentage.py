n=int(input())
a=[]
for i in range(0,n):
    k=input().split()
    a.insert(len(a),list(k))
l=input()
for i in range ( 0 , n ):
    if (a[i][0]==l):
        so=(float(a[i][1])+float(a[i][2])+float(a[i][3]))/3
        break
print(f"{so:.2f}")