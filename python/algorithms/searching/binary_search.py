"""
Binary Search works by repeatedly dividing
in half the portion of the list
that could contain the item, until you've
narrowed down the possible locations to just one.

"""

# Binary search algorithm
def binary_search(array, element):
  left = 0
  right = len(array) - 1

  while left <= right:
    middle = left + (right - left) // 2
    if array[middle] == element:
      return middle
    elif array[middle] < element:
      left = middle + 1
    else:
      right = middle - 1
  return -1

# this function to find the element
def find_element(array, element):
  position = binary_search(array, element)
  if position != -1:
    print(f"{element} found at position {position}")
  else:
    print(f"No results")

# this function to do the search
def print_list(array, element_to_find):
  print(f"List = {array}")
  print(f"Searching for : {element_to_find}")
  find_element(array, element_to_find)
  print("")

"""
Here I will a list where to find
a member element passed as argument

"""

list = [121, 12, 1, 0, 457, 5, 65, 69]
print_list(list, 0)
