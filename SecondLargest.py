def findSecondLargest(arr):
    if len(arr) < 2:
        return -1
    largest = -1
    second_largest = -1
    for x in arr:
        if x > largest:
            second_largest = largest
            largest = x
        elif x < largest and x > second_largest:
            second_largest = x
    return second_largest
arr=list(map(int,input("enter the elements:").split()))
sec_largest=findSecondLargest(arr)
if sec_largest==-1:
    print("No second largest element")
else:
    print("second largest element is:",sec_largest)
