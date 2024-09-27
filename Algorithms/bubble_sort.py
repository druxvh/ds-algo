def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def modified_bubble_sort(arr):
    for i in range(1, len(arr)):
        swapped = False
        for j in range(len(arr)-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr




'''
l = [2,4,23,1,3,10,32,42,53,325,6,11,23,53,22,45]
bubble_sort(l)
print(l)
'''