arr=list(map(int,input("enter the array elements:").split()))
n=len(arr)+1
total_sum=n*(n+1)//2
arr_sum=sum(arr)
missing_no=total_sum-arr_sum
print("The missing number is:",missing_no)