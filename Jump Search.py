import math

def jumpy(arr, x):

    step=math.sqrt(len(arr))
    prev=0

    while arr[int(min(step,len(arr))-1)] < x:
        prev = step
        step += math.sqrt(len(arr))
        if prev >= len(arr):
            return -1
        
    while arr[int(prev)] < x:
        prev += 1

        if prev == min(step, len(arr)):
            return -1
    
    if arr[int(prev)] == x:
        return int(prev)
    
    return -1

arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ]
x = 5

result= jumpy(arr, x)

print("Number", x, "is found at index" ,str(result))