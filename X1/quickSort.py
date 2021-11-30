def partition(arr,l,h):
    i = ( l - 1 )
    x = arr[h]
  
    for j in range(l , h):
        if   arr[j] <= x:

            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
  
    arr[i+1],arr[h] = arr[h],arr[i+1]
    return (i+1)

def quickSort(arr): #l=0 h=n-1
    size = len(arr)
    stack = [0] * (size)
    top = -1
    top = top + 1
    stack[top] = 0
    top = top + 1
    stack[top] = size-1
    while top >= 0:

        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1
  
        p = partition( arr, l, h )
  
        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

arr = [4, 3, 5, 2, 1, 3, 2, 3]
quickSort(arr)
print (f"Sorted array is: {arr}")