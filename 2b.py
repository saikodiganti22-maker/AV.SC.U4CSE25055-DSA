num_elements = int(input("How many numbers do you want to add to the list? "))
user_list = [] 
for i in range(num_elements):
    item = int(input(f"Enter number {i + 1}: "))
    user_list.append(item)
user_list.sort()
print(f"\nYour sorted list for searching: {user_list}")
target = int(input("Enter the number you want to search for: "))
low = 0
high = len(user_list) - 1
found_index = -1
while low <= high:
    mid = (low + high) // 2  
    
    if user_list[mid] == target:
        found_index = mid  
        break
    elif user_list[mid] < target:
        low = mid + 1    
    else:
        high = mid - 1      
if found_index != -1:
    print(f" Found! '{target}' is at index {found_index} in the sorted list.")
else:
    print(f" '{target}' was not found in the list.")

    
