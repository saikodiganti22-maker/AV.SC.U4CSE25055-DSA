num_elements = int(input("How many numbers do you want to add to the list? "))
user_list = []
for i in range(num_elements):
    item = int(input(f"Enter number {i + 1}: "))
    user_list.append(item)
print(f"\nOriginal unsorted list: {user_list}")
def bubble_sort(user_list):
  n = len(user_list)
  for i in range(n):
    for j in range(0, n - i - 1):
        if user_list[j] > user_list[j + 1]:
            user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
  print(f"Sorted list: {user_list}")
bubble_sort(user_list)
