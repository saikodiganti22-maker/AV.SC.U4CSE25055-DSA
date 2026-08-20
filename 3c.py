def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
user_input = input("Enter numbers separated by spaces: ")
data = [int(num) for num in user_input.split()]
print("Original list:", data)
insertion_sort(data)
print("Sorted list:  ", data)
