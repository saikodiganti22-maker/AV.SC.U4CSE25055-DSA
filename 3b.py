def selection_sort(arr):
       n=len(arr)
       for i in range(n-1):
           min_index=i
           for j in range(i+1,n):
               if arr[j]<arr[min_index]:
                   min_index=j
           arr[i],arr[min_index]=arr[min_index],arr[i]
       return arr
arr = int(input("How many numbers do you want to add to the list? "))
user_list = []
for i in range( arr):
    item = int(input(f"Enter number {i + 1}: "))
    arr.append(item)
print(f"\nOriginal unsorted list: { arr}")

