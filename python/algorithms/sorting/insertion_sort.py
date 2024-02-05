"""
Insertion Sort is a simple sorting algorithm that
builds the final sorted array one element at a time.

"""

def insertionSort(array):
  # Looping al along the array elements
  for i in range(1, len(array)):
    key = array[i]
    j = i-1
    while j >= 0 and array[j] > key:
      array[j+1] = array[j]
      j -= 1
    array[j+1] = key
  return array

def print_list(arr, tag):
    print(f"This is the {tag} List = {arr}")

"""
Here I will give some unsorted list
and then print it before and after insertionSort

"""

unsorted_list = [121, 12, 1, 0, 457, 5, 65, 69, 32]
print_list(unsorted_list, "unsorted")
print_list(insertionSort(unsorted_list), "sorted")

