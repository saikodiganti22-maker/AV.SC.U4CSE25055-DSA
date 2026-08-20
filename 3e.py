def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]   
    left = [x for x in arr if x < pivot]     
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot]       
    return quick_sort(left) + middle + quick_sort(right)
user_input = input("Enter numbers separated by spaces: ")
data = [int(num) for num in user_input.split()]
print("Original list:", data)
quick_sort(data)
print("Sorted list:  ", data)
