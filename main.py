import random

def binary_search(arr, low, high, x):
    #Check base case
    if high  >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        #if element is smaller than mid,then it can only be present in left subarry
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)

        #else the element can only be present in right subarray
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        #Element is not present in the array
        return -1
    # Test array

arr = []
x = 78

for i in range(1, 100):
    arr.append(i)

#Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")


x = 1
while x < 300:
    x += 2
    print(x)
