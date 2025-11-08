arr=list(map(int,input("enter the array elements:").split()))
n=len(arr)
leaders=[]
count=0
for i in range(0,n):
    for j in range(i+1,n):
        if arr[i]>=arr[j]:
            count+=1
    if count==n-i-1:
        leaders.append(arr[i])
    count=0
print("leaders in the array are:",leaders)