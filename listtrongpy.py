x = int(input())
y = int(input())
z = int(input())
n = int(input())
a=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
           if (i+j+k!=n): a.insert(len(a),[i,j,k])
print(a) 
