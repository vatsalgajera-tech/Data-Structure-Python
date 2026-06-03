def LinearSearch(arr,key):
    for i in arr:
        if key == i:
            print(f"{key} Found")
            return
    print(f"{key} Not Found")
    
def BinarySearch(arr,key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == key:
            print(f"{key} Found")
            return
        if arr[middle] > key:
            right = middle - 1
        else:
            left = middle + 1
    print(f"{key} Not Found")
        
arr = [4,4556,67,76,54,3,2,2,5,7,78]
LinearSearch(arr,4556)
LinearSearch(arr,456)
sorted_arr = sorted(arr)
BinarySearch(sorted_arr,4556)
BinarySearch(sorted_arr,456)