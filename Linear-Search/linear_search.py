def linear_search(list, target):
    ''' 
    Returns the target when found in the list else returns none
    '''
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    
    return None
        

def verify(index):
    if index is not None:
        print("Target found at index:", index + 1)
    else:
        print("Target not found in the list")

numbers = [10,20,30,40,50,60,70,80,90,100]

result = linear_search(numbers, 50)
print("Numbers: ", numbers)
verify(result)