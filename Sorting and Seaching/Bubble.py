def bubble(arr):
    while True:
        swap = False
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swap = True
        if (not swap):
            break
    return arr
        
arr = [34,54,67,78,1,3,5,45,8,9,56]
print(bubble(arr))