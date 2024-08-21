new_list = [1,2,3]

# To check whether the item is in the array (linear runtime)
if 1 in new_list: print(True)
    # or
for n in new_list:
    if n == 1:
        print(True)
        break

# Insert (linear runtime) -> iterates and forwards each element

new_list.insert(3,4)

# Append (constant time) -> simply adds the item into the end of the list and doesn't cost the runtime cost as in the Insert function.

new_list.append(6)

# Joining or extending a list
new_list.extend([5,6,7,8,9])

# Deleting an item from a list (linear runtime)
new_list.pop()
new_list.remove()

print(new_list)