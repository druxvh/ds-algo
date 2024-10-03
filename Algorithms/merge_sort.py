def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    m = len(arr) // 2
    left = mergesort(arr[:m])
    right = mergesort(arr[m:])
    return merge(left,right)

def merge(left, right):
    arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
        
    arr.extend(left[i:])
    arr.extend(right[j:])

    return arr

'''
a = [5,1,4,2,3]
print(mergesort(a))
'''