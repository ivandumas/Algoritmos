def mergeSort(arr):
    if len(arr) > 1:
        
        m = len(arr)//2

        left = arr[:m]
        right = arr[m:]

        left = mergeSort(left)
        right = mergeSort(right)

        i = 0
        j = 0
        res = []
        
        while i < len(left) and j < len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        
        while i < len(left): #In case there is any item left in left
            res.append(left[i])
            i += 1

        while j < len(right): #In case there is any item left in right
            res.append(right[j])
            j += 1
        
        return res
    return arr

if __name__=="__main__":
    arr = [18,5,4,17,30,12,24,4,3,6]
    print(mergeSort(arr))
