def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1:], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Target found in the list: ", result)

numbers = [10,20,30,40,50,60,70,80,90,100]

result = recursive_binary_search(numbers, 1010)
print("Numbers: ", numbers)
verify(result)