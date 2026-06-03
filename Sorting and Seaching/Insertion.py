def insertionSort(arr):
    for i in range(1,len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = k
    return arr

arr = [34,54,67,78,1,3,5,45,8,9,56]
print(insertionSort(arr))