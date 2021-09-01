def binarySearch(arr,k):
    r = len(arr) - 1
    l = 0
    while (l <= r):
        m = (l+r)//2 #determina la mitad
        if k == arr[m]: return m
        elif (k < arr[m]) : r = m - 1
        else: l = m + 1
    return -1

if __name__ == "__main__":
    arr = [3, 4, 5, 6, 12, 17, 18, 24, 30, 33]
    
    result = binarySearch(arr,17)
    if result != -1:
        print ("El elemento está en la posición % d" % result)
    else:
        print ("El elemento no existe en el array")
