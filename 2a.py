num_elements = int(input("How many items do you want to add to the list? "))
user_list = [] 
for i in range(num_elements):
    item = input(f"Enter item {i + 1}: ")
    user_list.append(item) 
target = input("Enter the item you want to search for: ")
found_index = -1
for index in range(len(user_list)):
    if user_list[index] == target:
        found_index = index
        break 
if found_index != -1:
    print(f" Found! '{target}' is at index {found_index}.")
else:
    print(f" '{target}' was not found in the list.")
