N=int(input())
arr=list(map(int,input().split()))
for i in reversed(range(N)):
    if arr[i]%2!=0:
        print(arr[i])
        break