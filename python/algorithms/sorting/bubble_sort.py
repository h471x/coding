def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
        swapped = True
    if not swapped:
      break

  return arr

"""
Here I will give some unsorted list
and then print it before and after bubble_sort
"""
def print_list(arr, tag):
  print(f"This is the {tag} List = {arr}")

unsorted_list = [121, 12, 1, 0, 457, 5, 65, 69, 32]
print_list(unsorted_list, "unsorted")
print_list(bubble_sort(unsorted_list), "sorted")

