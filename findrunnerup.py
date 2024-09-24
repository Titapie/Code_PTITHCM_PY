n = int(input())

k=input()
arr=list(map(int,k.split()))
arr.sort()

for i in range(1,n,):
    if (arr[n-i]!=arr[n-1]) :
        print(arr[n-i])
        break
    