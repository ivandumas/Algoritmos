def heapsort(arr):
    size = len(arr)
    maxheap(arr,size)
    for i in range (size-1,0,-1):
        arr[0],arr[i] = arr[i], arr[0]
        size -= 1
        heapify(arr,size,0)
    
    return arr


def maxheap(arr,size):
    for i in range(size//2 - 1, -1, -1):
        heapify(arr, size, i)


def heapify(arr,size,root):
    left = 2 * root + 1
    right = 2 * root + 2

    if left < size and arr[root] < arr[left]:
        largest = left
    else: 
        largest = root
    
    if right < size and arr[largest] < arr[right]:
        largest = right
    
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]

        heapify(arr,size,largest)

if __name__=="__main__":
    arr = [18,5,4,17,30,12,24,4,3,6]
    print(heapsort(arr))


