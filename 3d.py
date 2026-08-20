def merge_sort(arr):
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr
        
    # Split the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]   # CORRECTED: Slice from start to mid
    right = arr[mid:]  # CORRECTED: Slice from mid to end
    
    # Recursively sort both halves
    merge_sort(left)
    merge_sort(right)
    
    # Merge the sorted halves back into the original array
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]  # CORRECTED: Changed right[i] to right[j]
            j += 1
        k += 1
        
    # Collect any remaining elements from the left slice
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    # Collect any remaining elements from the right slice
    while j < len(right):      # CORRECTED: Changed '<=' to '<'
        arr[k] = right[j]      # CORRECTED: Changed right[i] to right[j]
        j += 1
        k += 1

# Main driver execution
n = int(input("Enter number of elements: "))
arr = []
print("Enter elements:")
for _ in range(n):
    arr.append(int(input()))

merge_sort(arr)
print("Sorted Array:", arr)    # CORRECTED: Added arr to print statement
