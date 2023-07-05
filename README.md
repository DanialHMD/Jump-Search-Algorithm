# Jump-Search-Algorithm
Jump Search Algorithm is one more useful algorithm like Binary Search used for finding a specific value in a sorted array. Basicaly Jump Search is used to look into less elements than other algorithms like Linear Search.
> Linear Search uses a loop to look into every elemnt of array to find the match.
### How Does It Work?
Like I mentioned earlier Jump Search skips some elements so it can use less time and memory. The way it works can be explained with the example code I uploaded on this repository.
```
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
```
The code above is a function for Jump Search. In the beginning this function needs an array which can look into and compare, and a variable like `x` which contains the value or element we are looking for in the array.
> Note: Make sure that the array is sorted, otherwise you can't find the element.

On the next step we need to make block to be jumped, in each block we look if the indexes values are a match for our `x` value or not, if no we jump to the next block and do the same, but if theres a match, we use linear search to find the index that holds our value and return the index.

First loop(below) is a loop to look into the blocks and find the block that has our element:
```
while arr[int(min(step,len(arr))-1)] < x:
        prev = step
        step += math.sqrt(len(arr))
        if prev >= len(arr):
            return -1
```
If it doesn't find a match it will returns `-1` which means the value is not present in any block. But when it finds a match, it will close the loop and jumps to the next step.
```
while arr[int(prev)] < x:
        prev += 1

        if prev == min(step, len(arr)):
            return -1
```
In this part(above) like I mentioned, we start a linear search to see where is our element, if we reach the end of block it will return `-1` value that represents that element is not present.
And at the end if it finds the element it will return the index that holds our element.
#### Notes:
1. Make sure that the types of elemnts are the same(both the `x` and the array elements)
2. Make sure that the array is sorted.
