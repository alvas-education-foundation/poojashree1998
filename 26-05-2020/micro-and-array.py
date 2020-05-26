t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    if k>min(arr):
        print(k-min(arr))
    else:
        print("0")
