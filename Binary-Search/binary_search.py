def binary_search(list, target):
    first_element = 0
    last_element = len(list) - 1

    while first_element <= last_element:
        midpoint = (first_element + last_element) // 2 
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first_element = midpoint + 1
        else:
            last_element = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Target found at index:", index + 1)
    else:
        print("Target not found in the list")

numbers = [10,20,30,40,50,60,66,70,80,90,100]

result = binary_search(numbers, 66)
print("Numbers: ", numbers)
verify(result)