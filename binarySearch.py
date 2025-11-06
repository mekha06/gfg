def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            result = mid
            high = mid - 1

        elif arr[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
    return result

arr_input = input("enter the array elements:")
arr = list(map(int, arr_input.split()))

x = int(input("enter the key:"))

result = binarySearch(arr, x)

if result != -1:
    print("Element is present at smallest index", result)
else:
    print("Element is not present in array")