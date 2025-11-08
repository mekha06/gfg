arr1=list(map(int,input("enter the array elements:").split()))
arr2=list(map(int,input("enter the array elements:").split()))
is_subset=True
for i in arr1:
    if i not in arr2:
        is_subset=False
        break
if is_subset:
    print("arr1 is a subset of arr2")
else:
    print("arr1 is not a subset of arr2")
