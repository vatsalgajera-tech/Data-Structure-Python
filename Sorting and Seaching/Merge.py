def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr) // 2
    l = arr[:m]
    r = arr[m:]
    l = merge_sort(l)
    r = merge_sort(r)
    return merge(l,r)

def merge(l,r):
    n = []
    i = j = 0
    while len(l) > i and len(r) > j:
        if l[i] > r[j]:
            n.append(r[j])
            j+=1
        else:
            n.append(l[i])
            i+=1
    n.extend(l[i:])
    n.extend(r[j:])
    return n

a = [65,3,0,56,78,98,34,3,32,12]            
print(merge_sort(a))        