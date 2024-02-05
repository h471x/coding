"""
Merge Sort is an efficient, stable, and comparison-based
Divide and Conquer sorting algorithm, and its recursive.
It divides the input array into two halves, calls itselffor the
two halves, sorting them, and then merges the two sorted halves.

"""

def merge_sort(array):
  if len(array) > 1:
    middle = len(array) // 2
    left_elements = array[middle:]
    right_elements = array[:middle]

    merge_sort(left_elements)
    merge_sort(right_elements)

    merge(array, left_elements, right_elements)
  return array

def merge(array, left_elements, right_elements):
  i = j = k = 0

  # Merging the temporary array
  # back into array[]

  while i < len(left_elements) and j < len(right_elements):
    if left_elements[i] < right_elements[j]:
      array[k] = left_elements[i]
      i += 1
    else:
      array[k] = right_elements[j]
      j += 1
    k += 1

  # Copy the remaining elements
  # of left_elements[] if there are any
  while i < len(left_elements):
    array[k] = left_elements[i]
    i += 1
    k += 1

  # Copy the remaining elements
  # of right_elements[] if there are any
  while j < len(right_elements):
    array[k] = right_elements[j]
    j += 1
    k += 1

def print_list(arr, tag):
    print(f"This is the {tag} List = {arr}")

"""
Here I will give some unsorted list
and then print it before and after insertionSort

"""

unsorted_list = [121, 12, 1, 0, 457, 5, 65, 69, 32]
print_list(unsorted_list, "unsorted")
print_list(merge_sort(unsorted_list), "sorted")

